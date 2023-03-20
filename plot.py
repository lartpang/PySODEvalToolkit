# -*- coding: utf-8 -*-
import argparse
import textwrap

import numpy as np
import yaml

from metrics import draw_curves


def get_args():
    parser = argparse.ArgumentParser(
        description=textwrap.dedent(
            r"""
    INCLUDE:

    - Fm Curve
    - PR Curves

    NOTE:

    - Our method automatically calculates the intersection of `pre` and `gt`.
    - Currently supported pre naming rules: `prefix + gt_name_wo_ext + suffix_w_ext`

    EXAMPLES:

    python plot.py \
        --curves-npy output/rgbd-othermethods-curves.npy output/rgbd-ours-curves.npy \ # use the information from these npy files to draw curves
        --num-rows 1 \ # set the number of rows of the figure to 2
        --style-cfg configs/single_row_style.yml \ # specific the configuration file for the style of matplotlib
        --num-col-legend 1 \ # set the number of the columns of the legend in the figure to 1
        --mode pr \ # draw `pr` curves
        --our-methods Ours \ # specific the names of our own methods, they must be contained in the npy file
        --save-name ./output/rgbd-pr-curves # save the figure into `./output/rgbd-pr-curves.<ext_name>`, where `ext_name` will be specificed to the item `savefig.format` in the `--style-cfg`

    python plot.py \
        --curves-npy output/rgbd-othermethods-curves.npy output/rgbd-ours-curves.npy \
        --num-rows 2 \
        --style-cfg configs/two_row_style.yml \
        --num-col-legend 2 \
        --separated-legend \ # use a separated legend
        --mode fm \ # draw `fm` curves
        --our-methods OursV0 OursV1 \ # specific the names of our own methods, they must be contained in the npy file
        --save-name output/rgbd-fm \
        --alias-yaml configs/rgbd_aliases.yaml # aliases corresponding to methods and datasets you want to use
    """
        ),
        formatter_class=argparse.RawTextHelpFormatter,
    )
    parser.add_argument("--alias-yaml", type=str, help="Yaml file for datasets and methods alias.")
    parser.add_argument(
        "--style-cfg",
        type=str,
        required=True,
        help="Yaml file for plotting curves.",
    )
    parser.add_argument(
        "--curves-npys",
        required=True,
        type=str,
        nargs="+",
        help="Npy file for saving curve results.",
    )
    parser.add_argument(
        "--our-methods", type=str, nargs="+", help="Names of our methods for highlighting it."
    )
    parser.add_argument(
        "--num-rows", type=int, default=1, help="Number of rows for subplots. Default: 1"
    )
    parser.add_argument(
        "--num-col-legend", type=int, default=1, help="Number of columns in the legend. Default: 1"
    )
    parser.add_argument(
        "--mode",
        type=str,
        choices=["pr", "fm", "em"],
        default="pr",
        help="Mode for plotting. Default: pr",
    )
    parser.add_argument(
        "--separated-legend", action="store_true", help="Use the separated legend."
    )
    parser.add_argument("--sharey", action="store_true", help="Use the shared y-axis.")
    parser.add_argument("--save-name", type=str, help="the exported file path")
    args = parser.parse_args()

    return args


def main(args):
    method_aliases = dataset_aliases = None
    if args.alias_yaml:
        with open(args.alias_yaml, mode="r", encoding="utf-8") as f:
            aliases = yaml.safe_load(f)
        method_aliases = aliases.get("method")
        dataset_aliases = aliases.get("dataset")

    draw_curves.draw_curves(
        mode=args.mode,
        # 不同曲线的绘图配置
        axes_setting={
            # pr曲线的配置
            "pr": {
                "x_label": "Recall",
                "y_label": "Precision",
                "x_ticks": np.linspace(0.5, 1, 6),
                "y_ticks": np.linspace(0.7, 1, 6),
            },
            # fm曲线的配置
            "fm": {
                "x_label": "Threshold",
                "y_label": r"F$_{\beta}$",
                "x_ticks": np.linspace(0, 1, 6),
                "y_ticks": np.linspace(0.6, 1, 6),
            },
            # em曲线的配置
            "em": {
                "x_label": "Threshold",
                "y_label": r"E$_{m}$",
                "x_ticks": np.linspace(0, 1, 6),
                "y_ticks": np.linspace(0.7, 1, 6),
            },
        },
        curves_npy_path=args.curves_npys,
        row_num=args.num_rows,
        method_aliases=method_aliases,
        dataset_aliases=dataset_aliases,
        style_cfg=args.style_cfg,
        ncol_of_legend=args.num_col_legend,
        separated_legend=args.separated_legend,
        sharey=args.sharey,
        our_methods=args.our_methods,
        save_name=args.save_name,
    )


if __name__ == "__main__":
    args = get_args()
    main(args)
