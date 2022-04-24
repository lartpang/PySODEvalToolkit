# -*- coding: utf-8 -*-
import argparse
import os
import textwrap
import warnings

from metrics import cal_sod_matrics
from utils.generate_info import get_datasets_info, get_methods_info
from utils.misc import make_dir
from utils.recorders import METRIC_MAPPING


def get_args():
    parser = argparse.ArgumentParser(
        description=textwrap.dedent(
            r"""
    INCLUDE:

    - F-measure-Threshold Curve
    - Precision-Recall Curve
    - MAE
    - weighted F-measure
    - S-measure
    - max/average/adaptive F-measure
    - max/average/adaptive E-measure
    - max/average Precision
    - max/average Sensitivity
    - max/average Specificity
    - max/average F-measure
    - max/average Dice
    - max/average IoU

    NOTE:

    - Our method automatically calculates the intersection of `pre` and `gt`.
    - Currently supported pre naming rules: `prefix + gt_name_wo_ext + suffix_w_ext`

    EXAMPLES:

    python eval_all.py \
        --dataset-json configs/datasets/json/rgbd_sod.json \
        --method-json configs/methods/json/rgbd_other_methods.json configs/methods/json/rgbd_our_method.json --metric-npy output/rgbd_metrics.npy \
        --curves-npy output/rgbd_curves.npy \
        --record-tex output/rgbd_results.txt
    """
        ),
        formatter_class=argparse.RawTextHelpFormatter,
    )
    parser.add_argument("--dataset-json", required=True, type=str, help="Json file for datasets.")
    parser.add_argument(
        "--method-json", required=True, nargs="+", type=str, help="Json file for methods."
    )
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
    parser.add_argument(
        "--metric-names",
        type=str,
        nargs="+",
        default=["mae", "fm", "em", "sm", "wfm"],
        choices=METRIC_MAPPING.keys(),
        help="Names of metrics",
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
        methods_info_jsons=args.method_json,
        for_drawing=True,
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
        metric_names=args.metric_names,
        ncols_tqdm=119,
    )


if __name__ == "__main__":
    main()
