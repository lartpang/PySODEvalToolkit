# -*- coding: utf-8 -*-
import os
from collections import defaultdict

import numpy as np
import scipy.io as scio

from metrics.sod import draw_curves
from utils.generate_info import get_datasets_info, get_methods_info
from utils.misc import colored_print, make_dir
from utils.print_formatter import print_formatter
from utils.recorders import MetricExcelRecorder, TxtRecorder

"""
This file can be used to plot curves with the 'mat' files from Fan's project:
- <https://github.com/DengPingFan/CODToolbox>

Include:
- Fm Curve,
- PR Curves,
- MAE,
- max/mean/adaptive/weighted F-measure,
- Smeasure,
- max/mean/adaptive Emeasure.

NOTE:
* Our method automatically calculates the intersection of `pre` and `gt`.
    But it needs to have uniform naming rules for `pre` and `gt`.
"""

total_info = dict(
    rgb_cosod=dict(
        dataset="/home/lart/Coding/Py-SOD-VOS-EvalToolkit/configs/datasets/json/rgb_cosod.json",
        method="/home/lart/Coding/Py-SOD-VOS-EvalToolkit/configs/methods/json/rgb_cosod_methods.json",
    ),
    rgb_sod=dict(
        dataset="/home/lart/Coding/Py-SOD-VOS-EvalToolkit/configs/datasets/json/rgb_sod.json",
        method="/home/lart/Coding/Py-SOD-VOS-EvalToolkit/configs/methods/json/rgb_sod_methods.json",
    ),
    rgb_cod=dict(
        dataset="/home/lart/Coding/Py-SOD-VOS-EvalToolkit/configs/datasets/json/rgb_cod.json",
        method="/home/lart/Coding/Py-SOD-VOS-EvalToolkit/configs/methods/json/rgb_cod_methods.json",
    ),
    rgbd_sod=dict(
        dataset="/home/lart/Coding/Py-SOD-VOS-EvalToolkit/configs/datasets/json/rgbd_sod.json",
        method="/home/lart/Coding/Py-SOD-VOS-EvalToolkit/configs/methods/json/rgbd_sod_methods.json",
    ),
)


def export_valid_npy():
    """
    The function will save the results of all models on different datasets in a `npy` file in the
    form of a dictionary.
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

    for dataset_name in dataset_info.keys():
        # 使用dataset_name索引各个方法在不同数据集上的结果
        for method_name, method_info in drawing_info.items():
            method_result_path = method_info["path_dict"]

            # if dataset_name is None, `.get(dataset_name, other_value)` will return `other_value`.
            info_for_dataset = method_result_path.get(dataset_name, None)
            if info_for_dataset is None:
                colored_print(
                    msg=f"{method_name} does not have results on {dataset_name}", mode="warning"
                )
                continue

            mat_path = info_for_dataset.get("mat", None)
            if mat_path is None:
                colored_print(
                    msg=f"{method_name} does not have results on {dataset_name}", mode="warning"
                )
                continue

            method_result = scio.loadmat(mat_path)
            method_curves = {
                "p": method_result["column_Pr"].reshape(-1).round(num_bits).tolist(),
                "r": method_result["column_Rec"].reshape(-1).round(num_bits).tolist(),
                "fm": method_result["column_F"].reshape(-1).round(num_bits).tolist(),
            }
            method_metrics = {
                "maxF": method_result["maxFm"].reshape(-1).round(num_bits).item(),
                "avgF": method_result["meanFm"].reshape(-1).round(num_bits).item(),
                "adpF": method_result["adpFm"].reshape(-1).round(num_bits).item(),
                "maxE": method_result["maxEm"].reshape(-1).round(num_bits).item(),
                "avgE": method_result["meanEm"].reshape(-1).round(num_bits).item(),
                "adpE": method_result["adpEm"].reshape(-1).round(num_bits).item(),
                "wFm": method_result["wFm"].reshape(-1).round(num_bits).item(),
                "MAE": method_result["mae"].reshape(-1).round(num_bits).item(),
                "SM": method_result["Sm"].reshape(-1).round(num_bits).item(),
            }
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


if __name__ == "__main__":
    for_pr = True  # 绘制pr还是fm曲线

    data_type = "rgbd_sod"
    data_info = total_info[data_type]

    # 存放输出文件的文件夹
    output_path = "./output"

    # 包含所有待比较模型结果的信息和绘图配置的字典
    # 包含所有待比较模型结果的信息和绘图配置的字典
    dataset_info = get_datasets_info(datastes_info_json=data_info["dataset"])
    drawing_info = get_methods_info(
        methods_info_json=data_info["method"], for_drawing=True, our_name="SINet"
    )

    # 用来保存测试结果的文件的路径
    txt_path = os.path.join(output_path, f"{data_type}.txt")
    xlsx_path = os.path.join(output_path, f"{data_type}.xlsx")

    # 是否将评估结果到npy文件中，该文件可用来绘制pr和fm曲线
    save_npy = True
    # 保存曲线指标数据的文件路径
    curves_npy_path = os.path.join(output_path, data_type + "_" + "curves.npy")
    metrics_npy_path = os.path.join(output_path, data_type + "_" + "metrics.npy")

    row_num = 1

    # 不同曲线的绘图配置
    axes_setting = {
        # pr曲线的配置
        "pr": {
            # 横坐标标签
            "x_label": "Recall",
            # 纵坐标标签
            "y_label": "Precision",
            # 横坐标显示范围
            "x_lim": (0.1, 1),
            # 纵坐标显示范围
            "y_lim": (0.1, 1),
        },
        # fm曲线的配置
        "fm": {
            # 横坐标标签
            "x_label": "Threshold",
            # 纵坐标标签
            "y_label": r"F$_{\beta}$",
            # 横坐标显示范围
            "x_lim": (0, 1),
            # 纵坐标显示范围
            "y_lim": (0, 0.9),
        },
    }
    # 评估结果保留的小数点后数据的位数
    num_bits = 3

    # 是否保留之前的评估记录（针对txt_path文件有效）
    resume_record = True

    export_valid_npy()

    draw_curves(
        for_pr=for_pr,
        axes_setting=axes_setting,
        curves_npy_path=curves_npy_path,
        row_num=row_num,
        drawing_info=drawing_info,
        dataset_info=dataset_info,
    )
