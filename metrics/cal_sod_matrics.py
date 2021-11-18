# -*- coding: utf-8 -*-

import os
from collections import defaultdict
from functools import partial
from multiprocessing import RLock, pool

import numpy as np
from tqdm import tqdm

from utils.misc import get_gt_pre_with_name, get_name_list, make_dir
from utils.print_formatter import formatter_for_tabulate
from utils.recorders import MetricExcelRecorder, MetricRecorder, TxtRecorder


class Recorder:
    def __init__(
        self,
        txt_path,
        to_append,
        max_method_name_width,
        xlsx_path,
        sheet_name,
        dataset_names,
        metric_names,
    ):
        self.curves = defaultdict(dict)  # Two curve metrics
        self.metrics = defaultdict(dict)  # Six numerical metrics
        self.dataset_name = None

        self.txt_recorder = None
        if txt_path:
            self.txt_recorder = TxtRecorder(
                txt_path=txt_path,
                to_append=to_append,
                max_method_name_width=max_method_name_width,
            )

        self.excel_recorder = None
        if xlsx_path:
            self.excel_recorder = MetricExcelRecorder(
                xlsx_path=xlsx_path,
                sheet_name=sheet_name,
                row_header=["methods"],
                dataset_names=dataset_names,
                metric_names=metric_names,
            )

    def record_dataset_name(self, dataset_name):
        self.dataset_name = dataset_name
        if self.txt_recorder:
            self.txt_recorder.add_row(
                row_name="Dataset", row_data=dataset_name, row_start_str="\n"
            )

    def record(self, method_results, method_name):
        method_curves = method_results["sequential"]
        method_metrics = method_results["numerical"]

        self.curves[self.dataset_name][method_name] = method_curves
        self.metrics[self.dataset_name][method_name] = method_metrics

        if self.excel_recorder:
            self.excel_recorder(
                row_data=method_metrics, dataset_name=self.dataset_name, method_name=method_name
            )
        if self.txt_recorder:
            self.txt_recorder(method_results=method_metrics, method_name=method_name)


def cal_sod_matrics(
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
    use_mp: bool = False,
):
    """
    Save the results of all models on different datasets in a `npy` file in the form of a
    dictionary.

    ::

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

    :param sheet_name: the type of the sheet in xlsx file
    :param txt_path: the path of the txt for saving results
    :param to_append: whether to append results to the original record
    :param xlsx_path: the path of the xlsx file for saving results
    :param methods_info: the method information
    :param datasets_info: the dataset information
    :param curves_npy_path: the npy file path for saving curve data
    :param metrics_npy_path: the npy file path for saving metric values
    :param num_bits: the number of bits used to format results
    :param num_workers: the number of workers of multiprocessing or multithreading
    :param use_mp: using multiprocessing or multithreading
    """
    recorder = Recorder(
        txt_path=txt_path,
        to_append=to_append,
        max_method_name_width=max([len(x) for x in methods_info.keys()]),  # 显示完整名字
        xlsx_path=xlsx_path,
        sheet_name=sheet_name,
        dataset_names=sorted(datasets_info.keys()),
        metric_names=["sm", "wfm", "mae", "adpf", "avgf", "maxf", "adpe", "avge", "maxe"],
    )

    for dataset_name, dataset_path in datasets_info.items():
        recorder.record_dataset_name(dataset_name)

        # 获取真值图片信息
        gt_info = dataset_path["mask"]
        gt_root = gt_info["path"]
        gt_ext = gt_info["suffix"]
        # 真值名字列表
        gt_index_file = dataset_path.get("index_file")
        if gt_index_file:
            gt_name_list = get_name_list(data_path=gt_index_file, name_suffix=gt_ext)
        else:
            gt_name_list = get_name_list(data_path=gt_root, name_suffix=gt_ext)
        assert len(gt_name_list) > 0, "there is not ground truth."

        # ==>> test the intersection between pre and gt for each method <<==
        tqdm.set_lock(RLock())
        pool_cls = pool.Pool if use_mp else pool.ThreadPool
        procs = pool_cls(
            processes=num_workers, initializer=tqdm.set_lock, initargs=(tqdm.get_lock(),)
        )
        procs_idx = 0
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
            pre_name_list = get_name_list(
                data_path=pre_root,
                name_prefix=pre_prefix,
                name_suffix=pre_suffix,
            )

            # get the intersection
            eval_name_list = sorted(list(set(gt_name_list).intersection(pre_name_list)))
            if len(eval_name_list) == 0:
                tqdm.write(f"{method_name} does not have results on {dataset_name}")
                continue

            procs.apply_async(
                func=evaluate_data,
                kwds=dict(
                    names=eval_name_list,
                    num_bits=num_bits,
                    pre_root=pre_root,
                    pre_prefix=pre_prefix,
                    pre_suffix=pre_suffix,
                    gt_root=gt_root,
                    gt_ext=gt_ext,
                    desc=f"[{dataset_name}({len(gt_name_list)}):{method_name}({len(pre_name_list)})]",
                    proc_idx=procs_idx,
                    blocking=use_mp,
                ),
                callback=partial(recorder.record, method_name=method_name),
            )
            procs_idx += 1
        procs.close()
        procs.join()

    if curves_npy_path:
        make_dir(os.path.dirname(curves_npy_path))
        np.save(curves_npy_path, recorder.curves)
        print(f"All curves has been saved in {curves_npy_path}")
    if metrics_npy_path:
        make_dir(os.path.dirname(metrics_npy_path))
        np.save(metrics_npy_path, recorder.metrics)
        print(f"All metrics has been saved in {metrics_npy_path}")
    formatted_string = formatter_for_tabulate(recorder.metrics)
    print(f"All methods have been evaluated:\n{formatted_string}")


def evaluate_data(
    names,
    num_bits,
    gt_root,
    gt_ext,
    pre_root,
    pre_prefix,
    pre_suffix,
    desc="",
    proc_idx=None,
    blocking=True,
):
    metric_recoder = MetricRecorder()
    # https://github.com/tqdm/tqdm#parameters
    # https://github.com/tqdm/tqdm/blob/master/examples/parallel_bars.py
    tqdm_bar = tqdm(
        names,
        total=len(names),
        desc=desc,
        position=proc_idx,
        ncols=79,
        lock_args=None if blocking else (False,),
    )
    for name in tqdm_bar:
        gt, pre = get_gt_pre_with_name(
            gt_root=gt_root,
            pre_root=pre_root,
            img_name=name,
            pre_prefix=pre_prefix,
            pre_suffix=pre_suffix,
            gt_ext=gt_ext,
            to_normalize=False,
        )
        metric_recoder.update(pre=pre, gt=gt)
    method_results = metric_recoder.show(num_bits=num_bits, return_ndarray=False)
    return method_results
