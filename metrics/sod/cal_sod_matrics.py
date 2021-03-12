# -*- coding: utf-8 -*-

import os
from collections import defaultdict

import numpy as np
from tqdm import tqdm

from utils.misc import colored_print, get_gt_pre_with_name, get_name_list, make_dir
from utils.print_formatter import print_formatter
from utils.recorders import MetricExcelRecorder, MetricRecorder, TxtRecorder


def cal_sod_matrics(
    data_type: str = "rgb_sod",
    txt_path: str = "",
    resume_record: bool = True,
    xlsx_path: str = "",
    drawing_info: dict = None,
    dataset_info: dict = None,
    skipped_datasets: list = None,
    save_npy: bool = True,
    curves_npy_path: str = "./curves.npy",
    metrics_npy_path: str = "./metrics.npy",
    num_bits: int = 3,
):
    """
    Save the results of all models on different datasets in a `npy` file in the form of a
    dictionary.
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
    curves = defaultdict(dict)  # Two curve metrics
    metrics = defaultdict(dict)  # Six numerical metrics

    txt_recoder = TxtRecorder(
        txt_path=txt_path,
        resume=resume_record,
        max_method_name_width=max([len(x) for x in drawing_info.keys()]),  # 显示完整名字
    )
    excel_recorder = MetricExcelRecorder(
        xlsx_path=xlsx_path,
        sheet_name=data_type,
        row_header=["methods"],
        dataset_names=sorted(list(dataset_info.keys())),
        metric_names=["sm", "wfm", "mae", "adpf", "avgf", "maxf", "adpe", "avge", "maxe"],
    )

    for dataset_name, dataset_path in dataset_info.items():
        if dataset_name in skipped_datasets:
            colored_print(msg=f"{dataset_name} will be skipped.", mode="warning")
            continue

        txt_recoder.add_row(row_name="Dataset", row_data=dataset_name, row_start_str="\n")

        # 获取真值图片信息
        gt_info = dataset_path["mask"]
        gt_root = gt_info["path"]
        gt_ext = gt_info["suffix"]
        # 真值名字列表
        gt_index_file = dataset_path.get("index_file")
        if gt_index_file:
            gt_name_list = get_name_list(data_path=gt_index_file, file_ext=gt_ext)
        else:
            gt_name_list = get_name_list(data_path=gt_root, file_ext=gt_ext)
        assert len(gt_name_list) > 0, "there is not ground truth."

        # ==>> test the intersection between pre and gt for each method <<==
        for method_name, method_info in drawing_info.items():
            method_root = method_info["path_dict"]
            method_dataset_info = method_root.get(dataset_name, None)
            if method_dataset_info is None:
                colored_print(
                    msg=f"{method_name} does not have results on {dataset_name}", mode="warning"
                )
                continue

            # 预测结果存放路径下的图片文件名字列表和扩展名称
            pre_ext = method_dataset_info["suffix"]
            pre_root = method_dataset_info["path"]
            pre_name_list = get_name_list(data_path=pre_root, file_ext=pre_ext)

            # get the intersection
            eval_name_list = sorted(list(set(gt_name_list).intersection(set(pre_name_list))))
            num_names = len(eval_name_list)

            if num_names == 0:
                colored_print(
                    msg=f"{method_name} does not have results on {dataset_name}", mode="warning"
                )
                continue

            colored_print(
                f"Evaluating {method_name} with {num_names} images"
                f" (G:{len(gt_name_list)},P:{len(pre_name_list)}) images on dataset {dataset_name}"
            )

            metric_recoder = MetricRecorder()
            tqdm_bar = tqdm(
                eval_name_list, total=num_names, leave=False, ncols=119, desc=f"[{dataset_name}]"
            )
            for img_name in tqdm_bar:
                gt, pre = get_gt_pre_with_name(
                    gt_root=gt_root,
                    pre_root=pre_root,
                    img_name=img_name,
                    pre_ext=pre_ext,
                    gt_ext=gt_ext,
                    to_normalize=False,
                )
                metric_recoder.update(pre=pre, gt=gt)
            method_results = metric_recoder.show(num_bits=num_bits, return_ndarray=False)
            method_curves = method_results["sequential"]
            method_metrics = method_results["numerical"]
            curves[dataset_name][method_name] = method_curves
            metrics[dataset_name][method_name] = method_metrics

            excel_recorder(
                row_data=method_metrics, dataset_name=dataset_name, method_name=method_name
            )
            txt_recoder(method_results=method_metrics, method_name=method_name)

    if save_npy:
        make_dir(os.path.dirname(curves_npy_path))
        np.save(curves_npy_path, curves)
        np.save(metrics_npy_path, metrics)
        colored_print(f"all methods have been saved in {curves_npy_path} and {metrics_npy_path}")
    formatted_string = print_formatter(metrics)
    colored_print(f"all methods have been tested:\n{formatted_string}")
