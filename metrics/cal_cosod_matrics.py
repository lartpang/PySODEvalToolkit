# -*- coding: utf-8 -*-

import os
from collections import defaultdict

import numpy as np
from tqdm import tqdm

from utils.misc import (
    colored_print,
    get_gt_pre_with_name,
    get_name_with_group_list,
    make_dir,
)
from utils.print_formatter import formatter_for_tabulate
from utils.recorders import GroupedMetricRecorder, MetricExcelRecorder, TxtRecorder


def group_names(names: list) -> dict:
    grouped_data = defaultdict(list)
    for name in names:
        group_name, file_name = name.split("/")
        grouped_data[group_name].append(file_name)
    return grouped_data


def cal_cosod_matrics(
    data_type: str = "rgb_sod",
    txt_path: str = "",
    resume_record: bool = True,
    xlsx_path: str = "",
    drawing_info: dict = None,
    dataset_info: dict = None,
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
        txt_recoder.add_row(row_name="Dataset", row_data=dataset_name, row_start_str="\n")

        # 获取真值图片信息
        gt_info = dataset_path["mask"]
        gt_root = gt_info["path"]
        gt_ext = gt_info["suffix"]
        # 真值名字列表
        gt_index_file = dataset_path.get("index_file")
        if gt_index_file:
            gt_name_list = get_name_with_group_list(data_path=gt_index_file, file_ext=gt_ext)
        else:
            gt_name_list = get_name_with_group_list(data_path=gt_root, file_ext=gt_ext)
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
            pre_name_list = get_name_with_group_list(data_path=pre_root, file_ext=pre_ext)

            # get the intersection
            eval_name_list = sorted(list(set(gt_name_list).intersection(set(pre_name_list))))
            num_names = len(eval_name_list)

            if num_names == 0:
                colored_print(
                    msg=f"{method_name} does not have results on {dataset_name}", mode="warning"
                )
                continue

            grouped_data = group_names(names=eval_name_list)
            num_groups = len(grouped_data)

            colored_print(
                f"Evaluating {method_name} with {num_names} images and {num_groups} groups"
                f" (G:{len(gt_name_list)},P:{len(pre_name_list)}) images on dataset {dataset_name}"
            )

            group_metric_recorder = GroupedMetricRecorder()
            inter_group_bar = tqdm(
                grouped_data.items(),
                total=num_groups,
                leave=False,
                ncols=119,
                desc=f"[{dataset_name}]",
            )
            for group_name, names_in_group in inter_group_bar:
                intra_group_bar = tqdm(
                    names_in_group,
                    total=len(names_in_group),
                    leave=False,
                    ncols=119,
                    desc=f"({group_name})",
                )
                for img_name in intra_group_bar:
                    img_name_with_group = os.path.join(group_name, img_name)
                    gt, pre = get_gt_pre_with_name(
                        gt_root=gt_root,
                        pre_root=pre_root,
                        img_name=img_name_with_group,
                        pre_ext=pre_ext,
                        gt_ext=gt_ext,
                        to_normalize=False,
                    )
                    group_metric_recorder.update(group_name=group_name, pre=pre, gt=gt)
            method_results = group_metric_recorder.show(num_bits=num_bits, return_ndarray=False)
            method_curves = method_results["sequential"]
            method_metrics = method_results["numerical"]
            curves[dataset_name][method_name] = method_curves
            metrics[dataset_name][method_name] = method_metrics

            excel_recorder(
                row_data=method_metrics, dataset_name=dataset_name, method_name=method_name
            )
            txt_recoder(method_results=method_metrics, method_name=method_name)

    if save_npy:
        make_dir(os.path.basename(curves_npy_path))
        np.save(curves_npy_path, curves)
        np.save(metrics_npy_path, metrics)
        colored_print(f"all methods have been saved in {curves_npy_path} and {metrics_npy_path}")
    formatted_string = formatter_for_tabulate(metrics)
    colored_print(f"all methods have been tested:\n{formatted_string}")
