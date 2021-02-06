# -*- coding: utf-8 -*-
import os
from collections import defaultdict
from pprint import pprint

import numpy as np
from matplotlib import colors
from tqdm import tqdm

from configs import total_info
from utils.misc import (
    get_gt_pre_with_name,
    get_name_with_group_list,
    get_valid_key_name,
    make_dir,
)
from utils.recorders import (
    CurveDrawer,
    MetricExcelRecorder,
    MetricRecorder,
    TxtRecorder,
)

"""
Include: Fm Curve/PR Curves/MAE/(max/mean/weighted) Fmeasure/Smeasure/Emeasure

NOTE:
* Our method automatically calculates the intersection of `pre` and `gt`.
    But it needs to have uniform naming rules for `pre` and `gt`.
"""


def group_names(names: list) -> dict:
    grouped_name_list = defaultdict(list)
    for name in names:
        group_name, file_name = name.split("/")
        grouped_name_list[group_name].append(file_name)
    return grouped_name_list


def mean_all_group_metrics(group_metric_recorder: dict):
    recorder = defaultdict(list)
    for group_name, metrics in group_metric_recorder.items():
        for metric_name, metric_array in metrics.items():
            recorder[metric_name].append(metric_array)
    results = {k: np.mean(np.vstack(v), axis=0) for k, v in recorder.items()}
    return results


def cal_all_metrics():
    """
    Save the results of all models on different datasets in a `npy` file in the form of a
    dictionary.
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
        metric_names=["sm", "wfm", "mae", "adpf", "avgf", "maxf", "adpe", "avge", "maxe"],
    )

    for dataset_name, dataset_path in cfg["dataset_info"].items():
        if dataset_name in cfg["skipped_names"]:
            print(f" ++>> {dataset_name} will be skipped.")
            continue

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
        for method_name, method_info in cfg["drawing_info"].items():
            method_root = method_info["path_dict"]
            method_dataset_info = method_root.get(dataset_name, None)
            if method_dataset_info is None:
                print(f" ==>> {method_name} does not have results on {dataset_name} <<== ")
                continue

            # 预测结果存放路径下的图片文件名字列表和扩展名称
            pre_ext = method_dataset_info["suffix"]
            pre_root = method_dataset_info["path"]
            pre_name_list = get_name_with_group_list(data_path=pre_root, file_ext=pre_ext)

            # get the intersection
            eval_name_list = sorted(list(set(gt_name_list).intersection(set(pre_name_list))))
            if len(eval_name_list) == 0:
                print(f" ==>> {method_name} does not have results on {dataset_name} <<== ")
                continue

            grouped_name_list = group_names(names=eval_name_list)
            print(
                f" ==>> It is evaluating {method_name} with"
                f" {len(eval_name_list)} images and {len(grouped_name_list)} groups"
                f" (G:{len(gt_name_list)},P:{len(pre_name_list)}) images <<== "
            )

            total_metric_recorder = {}
            inter_group_bar = tqdm(
                grouped_name_list.items(), total=len(grouped_name_list), leave=False, ncols=79
            )
            for group_name, names_in_group in inter_group_bar:
                inter_group_bar.set_description(f"({dataset_name}) group => {group_name}")

                metric_recoder = MetricRecorder()
                intra_group_bar = tqdm(
                    names_in_group, total=len(names_in_group), leave=False, ncols=79
                )
                for img_name in intra_group_bar:
                    intra_group_bar.set_description(f"processing => {img_name}")
                    img_name = "/".join([group_name, img_name])
                    gt, pre = get_gt_pre_with_name(
                        gt_root=gt_root,
                        pre_root=pre_root,
                        img_name=img_name,
                        pre_ext=pre_ext,
                        gt_ext=gt_ext,
                        to_normalize=False,
                    )
                    metric_recoder.update(pre=pre, gt=gt)
                total_metric_recorder[group_name] = metric_recoder.show(
                    bit_num=None
                )  # 保留原始数据  每组的结果
            all_results = mean_all_group_metrics(group_metric_recorder=total_metric_recorder)
            all_results["meanFm"] = all_results["fm"].mean()
            all_results["maxFm"] = all_results["fm"].max()
            all_results["meanEm"] = all_results["em"].mean()
            all_results["maxEm"] = all_results["em"].max()
            all_results = {k: v.round(cfg["bit_num"]) for k, v in all_results.items()}

            method_curve = {
                "prs": (
                    np.flip(all_results["p"]),
                    np.flip(all_results["r"]),
                ),
                "fm": np.flip(all_results["fm"]),
                "em": np.flip(all_results["em"]),
            }
            method_metric = {
                "maxF": all_results["maxFm"],
                "avgF": all_results["meanFm"],
                "adpF": all_results["adpFm"].tolist(),
                "maxE": all_results["maxEm"],
                "avgE": all_results["meanEm"],
                "adpE": all_results["adpEm"].tolist(),
                "wFm": all_results["wFm"].tolist(),
                "MAE": all_results["MAE"].tolist(),
                "SM": all_results["Sm"].tolist(),
            }
            qualitative_results[dataset_name.lower()][method_name] = method_curve
            quantitative_results[dataset_name.lower()][method_name] = method_metric

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

    curve_drawer = CurveDrawer(row_num=2, col_num=(len(cfg["dataset_info"].keys()) + 1) // 2)

    for idx, (dataset_name, dataset_path) in enumerate(cfg["dataset_info"].items()):
        dataset_name = get_valid_key_name(data_dict=qualitative_results, key_name=dataset_name)
        dataset_results = qualitative_results[dataset_name]

        for method_name, method_info in cfg["drawing_info"].items():
            method_name = get_valid_key_name(data_dict=dataset_results, key_name=method_name)
            method_results = dataset_results.get(method_name, None)
            if method_results:
                curve_drawer.add_subplot(idx + 1)
            else:
                print(f" ==>> {method_name} does not have results on {dataset_name} <<== ")
                continue

            if mode == "pr":
                assert isinstance(method_results["prs"], (list, tuple))
                y_data, x_data = method_results["prs"]
            else:
                y_data, x_data = method_results["fm"], np.linspace(1, 0, 255)

            curve_drawer.draw_method_curve(
                dataset_name=dataset_name,
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
    data_type = "rgb_cosod"
    data_info = total_info[data_type]
    output_path = "./output"  # 存放输出文件的文件夹

    cfg = {  # 针对多个模型评估比较的设置
        "dataset_info": data_info["dataset"],
        "drawing_info": data_info["method"]["drawing"],  # 包含所有待比较模型结果的信息和绘图配置的字典
        "selecting_info": data_info["method"]["selecting"],
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
        "colors": sorted(
            [
                color
                for name, color in colors.cnames.items()
                if name not in ["red", "white"] or not name.startswith("light") or "gray" in name
            ]
        ),
        "bit_num": 3,  # 评估结果保留的小数点后数据的位数
        "resume_record": True,  # 是否保留之前的评估记录（针对record_path文件有效）
        "skipped_names": [],
    }

    make_dir(output_path)
    cal_all_metrics()
    # draw_pr_fm_curve(for_pr=True)
