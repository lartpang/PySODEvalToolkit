# -*- coding: utf-8 -*-

import os
from collections import defaultdict
from functools import partial
from multiprocessing import pool
from threading import RLock as TRLock

import numpy as np
from tqdm import tqdm

from utils.misc import (
    get_gt_pre_with_name_and_group,
    get_name_with_group_list,
    make_dir,
)
from utils.print_formatter import formatter_for_tabulate
from utils.recorders import (
    BINARY_METRIC_MAPPING,
    GRAYSCALE_METRICS,
    GroupedMetricRecorder,
    MetricExcelRecorder,
    TxtRecorder,
)


class Recorder:
    def __init__(
        self,
        method_names,
        dataset_names,
        metric_names,
        *,
        txt_path,
        to_append,
        xlsx_path,
        sheet_name,
    ):
        self.curves = defaultdict(dict)  # Two curve metrics
        self.metrics = defaultdict(dict)  # Six numerical metrics
        self.method_names = method_names
        self.dataset_names = dataset_names

        self.txt_recorder = None
        if txt_path:
            self.txt_recorder = TxtRecorder(
                txt_path=txt_path,
                to_append=to_append,
                max_method_name_width=max([len(x) for x in method_names]),  # 显示完整名字
            )

        self.excel_recorder = None
        if xlsx_path:
            excel_metric_names = []
            for x in metric_names:
                if x in GRAYSCALE_METRICS:
                    if x == "em":
                        excel_metric_names.append(f"max{x}")
                        excel_metric_names.append(f"avg{x}")
                        excel_metric_names.append(f"adp{x}")
                    else:
                        config = BINARY_METRIC_MAPPING[x]
                        if config["kwargs"]["with_dynamic"]:
                            excel_metric_names.append(f"max{x}")
                            excel_metric_names.append(f"avg{x}")
                        if config["kwargs"]["with_adaptive"]:
                            excel_metric_names.append(f"adp{x}")
                else:
                    excel_metric_names.append(x)

            self.excel_recorder = MetricExcelRecorder(
                xlsx_path=xlsx_path,
                sheet_name=sheet_name,
                row_header=["methods"],
                dataset_names=dataset_names,
                metric_names=excel_metric_names,
            )

    def record(self, method_results, dataset_name, method_name):
        """Record results"""
        method_curves = method_results.get("sequential")
        method_metrics = method_results["numerical"]
        self.curves[dataset_name][method_name] = method_curves
        self.metrics[dataset_name][method_name] = method_metrics

    def export(self):
        """After evaluating all methods, export results to ensure the order of names."""
        for dataset_name in self.dataset_names:
            if dataset_name not in self.metrics:
                continue

            for method_name in self.method_names:
                dataset_results = self.metrics[dataset_name]
                method_results = dataset_results.get(method_name)
                if method_results is None:
                    continue

                if self.txt_recorder:
                    self.txt_recorder.add_row(row_name="Dataset", row_data=dataset_name)
                    self.txt_recorder(method_results=method_results, method_name=method_name)
                if self.excel_recorder:
                    self.excel_recorder(
                        row_data=method_results, dataset_name=dataset_name, method_name=method_name
                    )


def cal_metrics(
    sheet_name: str = "results",
    txt_path: str = "",
    to_append: bool = True,
    xlsx_path: str = "",
    methods_info: dict = None,
    datasets_info: dict = None,
    curves_npy_path: str = "./curves.npy",
    metrics_npy_path: str = "./metrics.npy",
    num_bits: int = 3,
    num_workers: int = 2,
    metric_names: tuple = ("sm", "wfm", "mae", "avgdice", "avgiou", "adpe", "avge", "maxe"),
    return_group: bool = False,
    start_idx: int = 1,
    end_idx: int = -1,
):
    """Save the results of all models on different datasets in a `npy` file in the form of a
    dictionary.

    Args:
        sheet_name (str, optional): The type of the sheet in xlsx file. Defaults to "results".
        txt_path (str, optional): The path of the txt for saving results. Defaults to "".
        to_append (bool, optional): Whether to append results to the original record. Defaults to True.
        xlsx_path (str, optional): The path of the xlsx file for saving results. Defaults to "".
        methods_info (dict, optional): The method information. Defaults to None.
        datasets_info (dict, optional): The dataset information. Defaults to None.
        curves_npy_path (str, optional): The npy file path for saving curve data. Defaults to "./curves.npy".
        metrics_npy_path (str, optional): The npy file path for saving metric values. Defaults to "./metrics.npy".
        num_bits (int, optional): The number of bits used to format results. Defaults to 3.
        num_workers (int, optional): The number of workers of multiprocessing or multithreading. Defaults to 2.
        metric_names (tuple, optional): Names of metrics. Defaults to ("sm", "wfm", "em", "mae", "dice", "iou").
        return_group (bool, optional): Whether to return the grouped results. Defaults to False.
        start_idx (int, optional): The index of the first frame in each gt sequence. Defaults to 1, it will skip the first frame. If it is set to None, the code will not skip frames.
        end_idx (int, optional): The index of the last frame in each gt sequence. Defaults to -1, it will skip the last frame. If it is set to None, the code will not skip frames.

    Returns:
        {
          dataset1:{
            method1:[fm, em, p, r],
            method2:[fm, em, p, r],
            .....
          },
          dataset2:{
            method1:[fm, em, p, r],
            method2:[fm, em, p, r],
            .....
          },
          ....
        }

    """
    metric_class = GroupedMetricRecorder

    method_names = tuple(methods_info.keys())
    dataset_names = tuple(datasets_info.keys())
    recorder = Recorder(
        method_names=method_names,
        dataset_names=dataset_names,
        metric_names=metric_names,
        txt_path=txt_path,
        to_append=to_append,
        xlsx_path=xlsx_path,
        sheet_name=sheet_name,
    )

    tqdm.set_lock(TRLock())
    procs = pool.ThreadPool(processes=num_workers, initializer=tqdm.set_lock,
                            initargs=(tqdm.get_lock(),))
    print(f"Create a {procs}).")
    name_sep = "<sep>"

    for dataset_name, dataset_path in datasets_info.items():
        # 获取真值图片信息
        gt_info = dataset_path["mask"]
        gt_root = gt_info["path"]
        gt_prefix = gt_info.get("prefix", "")
        gt_suffix = gt_info["suffix"]
        # 真值名字列表
        gt_index_file = dataset_path.get("index_file")
        if gt_index_file:
            gt_name_list = get_name_with_group_list(
                data_path=gt_index_file, name_prefix=gt_prefix, name_suffix=gt_suffix, sep=name_sep
            )
        else:
            gt_name_list = get_name_with_group_list(
                data_path=gt_root,
                name_prefix=gt_prefix,
                name_suffix=gt_suffix,
                start_idx=start_idx,
                end_idx=end_idx,
                sep=name_sep,
            )
        gt_info_pair = (gt_root, gt_prefix, gt_suffix)
        assert len(gt_name_list) > 0, f"there is not ground truth in {dataset_path}."

        # ==>> test the intersection between pre and gt for each method <<==
        for method_name, method_info in methods_info.items():
            method_root = method_info["path_dict"]
            method_dataset_info = method_root.get(dataset_name, None)
            if method_dataset_info is None:
                tqdm.write(f"{method_name} does not have results on {dataset_name}")
                continue

            # 预测结果存放路径下的图片文件名字列表和扩展名称
            pre_prefix = method_dataset_info.get("prefix", "")
            pre_suffix = method_dataset_info["suffix"]
            pre_root = method_dataset_info["path"]
            pre_name_list = get_name_with_group_list(
                data_path=pre_root, name_prefix=pre_prefix, name_suffix=pre_suffix, sep=name_sep
            )
            pre_info_pair = (pre_root, pre_prefix, pre_suffix)

            # get the intersection
            eval_name_list = sorted(set(gt_name_list).intersection(pre_name_list))
            if len(eval_name_list) == 0:
                tqdm.write(f"{method_name} does not have results on {dataset_name}")
                continue

            desc = f"[{dataset_name}({len(gt_name_list)}):{method_name}({len(pre_name_list)}->{len(eval_name_list)})]"
            kwargs = dict(
                names=eval_name_list,
                num_bits=num_bits,
                pre_info_pair=pre_info_pair,
                gt_info_pair=gt_info_pair,
                metric_names=metric_names,
                metric_class=metric_class,
                return_group=return_group,
                sep=name_sep,
                desc=desc,
            )
            callback = partial(recorder.record, dataset_name=dataset_name, method_name=method_name)
            procs.apply_async(func=evaluate, kwds=kwargs, callback=callback)
            # print(" -------------------- [DEBUG] -------------------- ")
            # callback(evaluate(**kwargs), dataset_name=dataset_name, method_name=method_name)
    procs.close()
    procs.join()

    recorder.export()
    if curves_npy_path:
        make_dir(os.path.dirname(curves_npy_path))
        np.save(curves_npy_path, recorder.curves)
        tqdm.write(f"All curves has been saved in {curves_npy_path}")
    if metrics_npy_path:
        make_dir(os.path.dirname(metrics_npy_path))
        np.save(metrics_npy_path, recorder.metrics)
        tqdm.write(f"All metrics has been saved in {metrics_npy_path}")
    formatted_string = formatter_for_tabulate(recorder.metrics, method_names, dataset_names)
    tqdm.write(f"All methods have been evaluated:\n{formatted_string}")


def evaluate(
    names,
    num_bits,
    pre_info_pair,
    gt_info_pair,
    metric_class,
    metric_names,
    return_group=False,
    sep="<sep>",
    desc="",
):
    group_names = sorted(set([n.split(sep)[0] for n in names]))
    metric_recoder = metric_class(group_names=group_names, metric_names=metric_names)
    # https://github.com/tqdm/tqdm#parameters
    # https://github.com/tqdm/tqdm/blob/master/examples/parallel_bars.py
    tqdm_bar = tqdm(names, total=len(names), desc=desc, ncols=78, lock_args=(False,))
    for name in tqdm_bar:
        group_name = name.split(sep)[0]
        gt, pre = get_gt_pre_with_name_and_group(
            img_name=name,
            pre_root=pre_info_pair[0],
            pre_prefix=pre_info_pair[1],
            pre_suffix=pre_info_pair[2],
            gt_root=gt_info_pair[0],
            gt_prefix=gt_info_pair[1],
            gt_suffix=gt_info_pair[2],
            to_normalize=False,
            sep=sep,
        )
        metric_recoder.step(
            group_name=group_name, pre=pre, gt=gt, gt_path=os.path.join(gt_info_pair[0], name)
        )

    # TODO: 打印的形式有待进一步完善
    method_results = metric_recoder.show(num_bits=num_bits, return_group=return_group)
    return method_results
