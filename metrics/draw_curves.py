# -*- coding: utf-8 -*-

from collections import OrderedDict

import numpy as np
from matplotlib import colors

from utils.recorders import CurveDrawer

# Align the mode with those in GRAYSCALE_METRICS
_YX_AXIS_NAMES = {
    "pr": ("precision", "recall"),
    "fm": ("fmeasure", None),
    "fmeasure": ("fmeasure", None),
    "em": ("em", None),
    "iou": ("iou", None),
    "dice": ("dice", None),
}


def draw_curves(
    mode: str,
    axes_setting: dict = None,
    curves_npy_path: list = None,
    row_num: int = 1,
    our_methods: list = None,
    method_aliases: OrderedDict = None,
    dataset_aliases: OrderedDict = None,
    style_cfg: dict = None,
    ncol_of_legend: int = 1,
    separated_legend: bool = False,
    sharey: bool = False,
    line_width=3,
    save_name=None,
):
    """A better curve painter!

    Args:
        mode (str): `pr` for PR curves, `fm` for F-measure curves, and `em' for E-measure curves.
        axes_setting (dict, optional): Setting for axes. Defaults to None.
        curves_npy_path (list, optional): Paths of curve npy files. Defaults to None.
        row_num (int, optional): Number of rows. Defaults to 1.
        our_methods (list, optional): Names of our methods. Defaults to None.
        method_aliases (OrderedDict, optional): Aliases of methods. Defaults to None.
        dataset_aliases (OrderedDict, optional): Aliases of datasets. Defaults to None.
        style_cfg (dict, optional): Config file for the style of matplotlib. Defaults to None.
        ncol_of_legend (int, optional): Number of columns for the legend. Defaults to 1.
        separated_legend (bool, optional): Use the separated legend. Defaults to False.
        sharey (bool, optional): Use a shared y-axis. Defaults to False.
        line_width (int, optional): Width of lines. Defaults to 3.
        save_name (str, optional): Name or path (without the extension format). Defaults to None.
    """
    save_name = save_name or mode
    y_axis_name, x_axis_name = _YX_AXIS_NAMES[mode]

    assert curves_npy_path
    if not isinstance(curves_npy_path, (list, tuple)):
        curves_npy_path = [curves_npy_path]

    curves = {}
    unique_method_names_from_npy = []
    for p in curves_npy_path:
        single_curves = np.load(p, allow_pickle=True).item()
        for dataset_name, method_infos in single_curves.items():
            curves.setdefault(dataset_name, {})
            for method_name, method_info in method_infos.items():
                curves[dataset_name][method_name] = method_info
                if method_name not in unique_method_names_from_npy:
                    unique_method_names_from_npy.append(method_name)
    dataset_names_from_npy = list(curves.keys())

    if dataset_aliases is None:
        dataset_aliases = OrderedDict({k: k for k in dataset_names_from_npy})
    else:
        for x in dataset_aliases.keys():
            if x not in dataset_names_from_npy:
                raise ValueError(f"{x} must be contained in\n{dataset_names_from_npy}")

    if method_aliases is not None:
        target_unique_method_names = []
        for x in method_aliases:
            if x in unique_method_names_from_npy:
                target_unique_method_names.append(x)
            # Only consider the name in npy is also in alias config.
            # if x not in unique_method_names_from_npy:
            #     raise ValueError(
            #         f"{x} must be contained in\n{sorted(unique_method_names_from_npy)}"
            #     )
    else:
        method_aliases = {}
        target_unique_method_names = unique_method_names_from_npy

    if our_methods is not None:
        our_methods.reverse()
        for x in our_methods:
            if x not in target_unique_method_names:
                raise ValueError(f"{x} must be contained in\n{target_unique_method_names}")
            # Put our methods into the head of the name list
            target_unique_method_names.pop(target_unique_method_names.index(x))
            target_unique_method_names.insert(0, x)
        # assert len(our_methods) <= len(line_styles)
    else:
        our_methods = []
    num_our_methods = len(our_methods)

    # Give each method a unique color and style.
    color_table = sorted(
        [
            color
            for name, color in colors.cnames.items()
            if name not in ["red", "white"] or not name.startswith("light") or "gray" in name
        ]
    )
    style_table = ["-", "--", "-.", ":", "."]

    unique_method_settings = OrderedDict()
    for i, method_name in enumerate(target_unique_method_names):
        if i < num_our_methods:
            line_color = "red"
            line_style = style_table[i % len(style_table)]
        else:
            other_idx = i - num_our_methods
            line_color = color_table[other_idx]
            line_style = style_table[other_idx % 2]

        unique_method_settings[method_name] = {
            "line_color": line_color,
            "line_label": method_aliases.get(method_name, method_name),
            "line_style": line_style,
            "line_width": line_width,
        }
    # ensure that our methods are drawn last to avoid being overwritten by other methods
    target_unique_method_names.reverse()

    curve_drawer = CurveDrawer(
        row_num=row_num,
        num_subplots=len(dataset_aliases),
        style_cfg=style_cfg,
        ncol_of_legend=ncol_of_legend,
        separated_legend=separated_legend,
        sharey=sharey,
    )

    for idx, (dataset_name, dataset_alias) in enumerate(dataset_aliases.items()):
        dataset_results = curves[dataset_name]

        for method_name in target_unique_method_names:
            method_setting = unique_method_settings[method_name]

            if method_name not in dataset_results:
                print(f"{method_name} will be skipped for {dataset_name}!")
                continue

            method_results = dataset_results[method_name]

            if y_axis_name is None:
                y_data = np.linspace(0, 1, 256)
            else:
                y_data = method_results[y_axis_name]
                assert isinstance(y_data, (list, tuple)), (method_name, method_results.keys())

            if x_axis_name is None:
                x_data = np.linspace(0, 1, 256)
            else:
                x_data = method_results[x_axis_name]
                assert isinstance(x_data, (list, tuple)), (method_name, method_results.keys())

            curve_drawer.plot_at_axis(idx, method_setting, x_data=x_data, y_data=y_data)
        curve_drawer.set_axis_property(idx, dataset_alias, **axes_setting[mode])
    curve_drawer.save(path=save_name)
