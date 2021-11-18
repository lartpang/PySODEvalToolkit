# -*- coding: utf-8 -*-
import argparse
import os
import sys
import warnings

sys.path.append("..")

from metrics import cal_sod_matrics
from utils.generate_info import get_datasets_info, get_methods_info
from utils.misc import make_dir


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
    parser.add_argument("--metric-npy", type=str, help="Npy file for saving metric results.")
    parser.add_argument("--curves-npy", type=str, help="Npy file for saving curve results.")
    parser.add_argument("--record-txt", type=str, help="Txt file for saving metric results.")
    parser.add_argument("--to-overwrite", action="store_true", help="To overwrite the txt file.")
    parser.add_argument("--record-xlsx", type=str, help="Xlsx file for saving metric results.")
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
        "--num-workers",
        type=int,
        default=4,
        help="Number of workers for multi-threading or multi-processing. Default: 4",
    )
    parser.add_argument(
        "--num-bits",
        type=int,
        default=3,
        help="Number of decimal places for showing results. Default: 3",
    )
    args = parser.parse_args()

    if args.metric_npy is not None:
        make_dir(os.path.dirname(args.metric_npy))
    if args.curves_npy is not None:
        make_dir(os.path.dirname(args.curves_npy))
    if args.record_txt is not None:
        make_dir(os.path.dirname(args.record_txt))
    if args.record_xlsx is not None:
        make_dir(os.path.dirname(args.record_xlsx))
    if args.to_overwrite and not args.record_txt:
        warnings.warn("--to-overwrite only works with a valid --record-txt")
    return args


def main():
    args = get_args()

    # 包含所有数据集信息的字典
    datasets_info = get_datasets_info(
        datastes_info_json=args.dataset_json,
        include_datasets=args.include_datasets,
        exclude_datasets=args.exclude_datasets,
    )
    # 包含所有待比较模型结果的信息的字典
    methods_info = get_methods_info(
        methods_info_json=args.method_json,
        include_methods=args.include_methods,
        exclude_methods=args.exclude_methods,
    )

    # 确保多进程在windows上也可以正常使用
    cal_sod_matrics.cal_sod_matrics(
        sheet_name="Results",
        to_append=not args.to_overwrite,
        txt_path=args.record_txt,
        xlsx_path=args.record_xlsx,
        methods_info=methods_info,
        datasets_info=datasets_info,
        curves_npy_path=args.curves_npy,
        metrics_npy_path=args.metric_npy,
        num_bits=args.num_bits,
        num_workers=args.num_workers,
        use_mp=False,
    )


if __name__ == "__main__":
    main()
