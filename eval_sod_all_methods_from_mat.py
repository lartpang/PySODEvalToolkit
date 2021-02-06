# -*- coding: utf-8 -*-
import math
import os
from collections import defaultdict
from pprint import pprint

import numpy as np
import scipy.io as scio

from configs import total_info
from utils.misc import make_dir
from utils.recorders import CurveDrawer, MetricExcelRecorder, TxtRecorder

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


def export_valid_npy():
    """
    The function will save the results of all models on different datasets in a `npy` file in the
    form of a dictionary.
    {
      dataset1:{
        method1:[(ps, rs), fs],
        method2:[(ps, rs), fs],
        .....
      },
      dataset2:{
        method1:[(ps, rs), fs],
        method2:[(ps, rs), fs],
        .....
      },
      ....
    }
    """
    qualitative_results = defaultdict(dict)  # Two curve metrics
    quantitative_results = defaultdict(dict)  # Six numerical metrics

    txt_recoder = TxtRecorder(
        txt_path=cfg["record_path"],
        resume=cfg["resume_record"],
        max_method_name_width=max([len(x) for x in cfg["drawing_info"].keys()]),  # 显示完整名字
        # max_method_name_width=10,  # 指定长度
    )
    excel_recorder = MetricExcelRecorder(
        xlsx_path=cfg["xlsx_path"],
        sheet_name=data_type,
        row_header=["methods"],
        dataset_names=sorted(list(cfg["dataset_info"].keys())),
        metric_names=["sm", "wfm", "mae", "adpfm", "avgfm", "maxfm", "adpem", "avgem", "maxem"],
    )

    for dataset_name in cfg["dataset_info"].keys():
        # 使用dataset_name索引各个方法在不同数据集上的结果
        for method_name, method_info in cfg["drawing_info"].items():
            method_result_path = method_info["path_dict"]

            # if dataset_name is None, `.get(dataset_name, other_value)` will return `other_value`.
            info_for_dataset = method_result_path.get(dataset_name, None)
            if info_for_dataset is None:
                print(f" ==>> {method_name} does not have results on {dataset_name} <<== ")
                continue

            mat_path = info_for_dataset.get("mat", None)
            if mat_path is None:
                print(f" ==>> {method_name} does not have results on {dataset_name} <<== ")
                continue

            method_result = scio.loadmat(mat_path)

            ps = method_result["column_Pr"].reshape(-1).round(cfg["bit_num"]).tolist()
            rs = method_result["column_Rec"].reshape(-1).round(cfg["bit_num"]).tolist()
            fm = method_result["column_F"].reshape(-1).round(cfg["bit_num"]).tolist()

            maxf = method_result["maxFm"].reshape(-1).round(cfg["bit_num"]).item()
            meanf = method_result["meanFm"].reshape(-1).round(cfg["bit_num"]).item()
            adpf = method_result["adpFm"].reshape(-1).round(cfg["bit_num"]).item()
            maxe = method_result["maxEm"].reshape(-1).round(cfg["bit_num"]).item()
            meane = method_result["meanEm"].reshape(-1).round(cfg["bit_num"]).item()
            adpe = method_result["adpEm"].reshape(-1).round(cfg["bit_num"]).item()
            wfm = method_result["wFm"].reshape(-1).round(cfg["bit_num"]).item()
            mae = method_result["mae"].reshape(-1).round(cfg["bit_num"]).item()
            sm = method_result["Sm"].reshape(-1).round(cfg["bit_num"]).item()

            method_curve = {"prs": (ps, rs), "fm": fm}
            method_metric = {
                "maxFm": maxf,
                "meanFm": meanf,
                "adpFm": adpf,
                "maxEm": maxe,
                "meanEm": meane,
                "adpEm": adpe,
                "wFm": wfm,
                "MAE": mae,
                "Sm": sm,
            }
            qualitative_results[dataset_name][method_name] = method_curve
            quantitative_results[dataset_name][method_name] = method_metric

            excel_recorder(
                row_data=method_metric, dataset_name=dataset_name, method_name=method_name
            )
            txt_recoder(method_results=method_metric, method_name=method_name)

    if cfg["save_npy"]:
        np.save(cfg["qualitative_npy_path"], qualitative_results)
        np.save(cfg["quantitative_npy_path"], quantitative_results)
        print(
            f" ==>> all methods have been saved in {cfg['qualitative_npy_path']} and "
            f"{cfg['quantitative_npy_path']} <<== "
        )

    print(f" ==>> all methods have been tested:")
    pprint(quantitative_results, indent=2, width=119)


def draw_pr_fm_curve(for_pr: bool = True):
    mode = "pr" if for_pr else "fm"
    mode_axes_setting = cfg["axes_setting"][mode]

    x_label, y_label = mode_axes_setting["x_label"], mode_axes_setting["y_label"]
    x_lim, y_lim = mode_axes_setting["x_lim"], mode_axes_setting["y_lim"]

    qualitative_results = np.load(
        os.path.join(cfg["qualitative_npy_path"]), allow_pickle=True
    ).item()

    row_num = 1
    curve_drawer = CurveDrawer(
        row_num=row_num, col_num=math.ceil(len(cfg["dataset_info"].keys()) / row_num)
    )

    for idx, dataset_name in enumerate(cfg["dataset_info"].keys()):
        # 与cfg[dataset_info]中的key保持一致
        dataset_results = qualitative_results[dataset_name]
        for method_name, method_info in cfg["drawing_info"].items():
            # 与cfg[drawing_info]中的key保持一致
            method_results = dataset_results.get(method_name, None)
            if method_results is None:
                print(f" ==>> {method_name} does not have results on {dataset_name} <<== ")
                continue

            if mode == "pr":
                assert isinstance(method_results["prs"], (list, tuple))
                y_data, x_data = method_results["prs"]
            else:
                y_data, x_data = method_results["fm"], np.linspace(1, 0, 256)

            curve_drawer.draw_method_curve(
                curr_idx=idx,
                dataset_name=dataset_name.upper(),
                method_curve_setting=method_info["curve_setting"],
                x_label=x_label,
                y_label=y_label,
                x_data=x_data,
                y_data=y_data,
                x_lim=x_lim,
                y_lim=y_lim,
            )
    curve_drawer.show()


if __name__ == "__main__":
    data_type = "rgbd_sod"
    data_info = total_info[data_type]
    output_path = "./output"  # 存放输出文件的文件夹

    cfg = {  # 针对多个模型评估比较的设置
        "dataset_info": data_info["dataset"],
        "drawing_info": data_info["method"]["drawing"],  # 包含所有待比较模型结果的信息和绘图配置的字典
        "record_path": os.path.join(output_path, f"{data_type}.txt"),  # 用来保存测试结果的文件的路径
        "xlsx_path": os.path.join(output_path, f"{data_type}.xlsx"),
        "save_npy": True,  # 是否将评估结果到npy文件中，该文件可用来绘制pr和fm曲线
        # 保存曲线指标数据的文件路径
        "qualitative_npy_path": os.path.join(
            output_path, data_type + "_" + "qualitative_results.npy"
        ),
        "quantitative_npy_path": os.path.join(
            output_path, data_type + "_" + "quantitative_results.npy"
        ),
        "axes_setting": {  # 不同曲线的绘图配置
            "pr": {  # pr曲线的配置
                "x_label": "Recall",  # 横坐标标签
                "y_label": "Precision",  # 纵坐标标签
                "x_lim": (0.1, 1),  # 横坐标显示范围
                "y_lim": (0.1, 1),  # 纵坐标显示范围
            },
            "fm": {  # fm曲线的配置
                "x_label": "Threshold",  # 横坐标标签
                "y_label": r"F$_{\beta}$",  # 纵坐标标签
                "x_lim": (0, 1),  # 横坐标显示范围
                "y_lim": (0, 0.9),  # 纵坐标显示范围
            },
        },
        "bit_num": 3,  # 评估结果保留的小数点后数据的位数
        "resume_record": False,  # 是否保留之前的评估记录（针对record_path文件有效）
        "skipped_names": [],
    }

    make_dir(output_path)
    export_valid_npy()
    # draw_pr_fm_curve(for_pr=True)
