# -*- coding: utf-8 -*-
import argparse
import json
import sys
from collections import OrderedDict

sys.path.append("..")

from metrics import draw_curves
from utils.generate_info import get_datasets_info, get_methods_info


def get_args():
    parser = argparse.ArgumentParser(
        description="""Include: Fm Curve/PR Curves/MAE/(max/mean/weighted) Fmeasure/Smeasure/Emeasure
    NOTE:
        Our method automatically calculates the intersection of `pre` and `gt`.
        Currently supported pre naming rules: `prefix + gt_name_wo_ext + suffix_w_ext`
    """,
        formatter_class=argparse.RawTextHelpFormatter,
    )
    parser.add_argument("--dataset-json", required=True, type=str, help="Json file for datasets.")
    parser.add_argument("--method-json", required=True, type=str, help="Json file for methods.")
    parser.add_argument(
        "--alias-json", type=str, help="Json file for name aliases of datasets and methods."
    )
    parser.add_argument(
        "--curves-npy", required=True, type=str, help="Npy file for saving curve results."
    )
    parser.add_argument("--our-method", type=str, help="Name of our method for highlighting it.")
    parser.add_argument(
        "--num-rows", type=int, default=1, help="Number of rows for subplots. Default: 1"
    )
    parser.add_argument(
        "--num-col-legend", type=int, default=1, help="Number of columns in the legend. Default: 1"
    )
    parser.add_argument(
        "--mode",
        type=str,
        choices=["pr", "fm"],
        default="pr",
        help="Mode for plotting. Default: pr",
    )
    parser.add_argument(
        "--include-methods",
        type=str,
        nargs="+",
        help="Names of only specific methods you want to evaluate.",
    )
    parser.add_argument(
        "--exclude-methods",
        type=str,
        nargs="+",
        help="Names of some specific methods you do not want to evaluate.",
    )
    parser.add_argument(
        "--include-datasets",
        type=str,
        nargs="+",
        help="Names of only specific datasets you want to evaluate.",
    )
    parser.add_argument(
        "--exclude-datasets",
        type=str,
        nargs="+",
        help="Names of some specific datasets you do not want to evaluate.",
    )
    parser.add_argument(
        "--separated-legend", action="store_true", help="Use the separated legend."
    )
    parser.add_argument("--sharey", action="store_true", help="Use the shared y-axis.")
    args = parser.parse_args()

    return args


def main():
    args = get_args()

    # 包含所有数据集信息的字典
    datasets_info = get_datasets_info(
        datastes_info_json=args.dataset_json,
        include_datasets=args.include_datasets,
        exclude_datasets=args.exclude_datasets,
    )
    # 包含所有待比较模型结果的信息和绘图配置的字典
    methods_info = get_methods_info(
        methods_info_json=args.method_json,
        for_drawing=True,
        our_name=args.our_method,
        include_methods=args.include_methods,
        exclude_methods=args.exclude_methods,
    )

    dataset_alias = {}
    method_alias = {}
    if args.alias_json:
        with open(args.alias_json, encoding="utf-8", mode="r") as f:
            alias = json.load(f, object_hook=OrderedDict)
            dataset_alias = alias["dataset"]
            method_alias = alias["method"]

    for method_name, method_info in methods_info.items():
        label_name = method_info["curve_setting"]["line_label"]
        method_info["curve_setting"]["line_label"] = method_alias.get(method_name, label_name)

    draw_curves.draw_curves(
        for_pr=args.mode == "pr",
        # 不同曲线的绘图配置
        axes_setting={
            # pr曲线的配置
            "pr": {
                # 横坐标标签
                "x_label": "Recall",
                # 纵坐标标签
                "y_label": "Precision",
                # 横坐标显示范围
                "x_lim": (0.5, 1),
                # 纵坐标显示范围
                "y_lim": (0.7, 1),
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
                "y_lim": (0.7, 1),
            },
        },
        curves_npy_path=args.curves_npy,
        row_num=args.num_rows,
        methods_info=methods_info,
        datasets_info=datasets_info,
        dataset_alias=dataset_alias,
        subplots_cfg={  # setting for subplots
            "left": 0.035,
            "bottom": 0.099,
            "right": 0.99,
            "top": 0.95,
            "wspace": 0.26,
            "hspace": 0.3,
        },
        font_cfg={
            "title": {
                "fontdict": {
                    "fontsize": 14,
                }
            },
            "label": {
                "fontdict": {
                    "fontsize": 12,
                }
            },
            "ticks": {
                "fontdict": {
                    "fontsize": 10,
                }
            },
            "legend": {
                "ncol": args.num_col_legend,
                "prop": {
                    "size": 10,
                },
            },
        },
        separated_legend=args.separated_legend,
        sharey=args.sharey,
    )


if __name__ == "__main__":
    main()
