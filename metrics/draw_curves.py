# -*- coding: utf-8 -*-

from collections import OrderedDict

import numpy as np
from matplotlib import colors

from utils.recorders import CurveDrawer


def draw_curves(
    for_pr: bool = True,
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
    line_styles=("-", "--"),
    line_width=3,
    save_name=None,
):
    """A better curve painter!

    Args:
        for_pr (bool, optional): Plot for PR curves or FM curves. Defaults to True.
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
        line_styles (tuple, optional): Styles of lines. Defaults to ("-", "--").
        line_width (int, optional): Width of lines. Defaults to 3.
        save_name (str, optional): Name or path (without the extension format). Defaults to None.
    """
    mode = "pr" if for_pr else "fm"
    save_name = save_name or mode
    mode_axes_setting = axes_setting[mode]

    x_label, y_label = mode_axes_setting["x_label"], mode_axes_setting["y_label"]
    x_ticks, y_ticks = mode_axes_setting["x_ticks"], mode_axes_setting["y_ticks"]

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
        dataset_aliases = {k: k for k in dataset_names_from_npy}
    else:
        for x in dataset_aliases.keys():
            if x not in dataset_names_from_npy:
                raise ValueError(f"{x} must be contained in\n{dataset_names_from_npy}")

    if method_aliases is not None:
        target_unique_method_names = list(method_aliases.keys())
        for x in target_unique_method_names:
            if x not in unique_method_names_from_npy:
                raise ValueError(
                    f"{x} must be contained in\n{sorted(unique_method_names_from_npy)}"
                )
    else:
        target_unique_method_names = unique_method_names_from_npy

    if our_methods is not None:
        for x in our_methods:
            if x not in target_unique_method_names:
                raise ValueError(f"{x} must be contained in\n{target_unique_method_names}")
        assert len(our_methods) <= len(line_styles)
    else:
        our_methods = []

    # Give each method a unique color.
    color_table = sorted(
        [
            color
            for name, color in colors.cnames.items()
            if name not in ["red", "white"] or not name.startswith("light") or "gray" in name
        ]
    )
    unique_method_settings = {}
    for i, method_name in enumerate(target_unique_method_names):
        if method_name in our_methods:
            line_color = "red"
            line_style = line_styles[our_methods.index(method_name)]
        else:
            line_color = color_table[i]
            line_style = line_styles[i % 2]
        line_label = (
            method_name if method_aliases is None else method_aliases.get(method_name, method_name)
        )

        unique_method_settings[method_name] = {
            "line_color": line_color,
            "line_style": line_style,
            "line_label": line_label,
            "line_width": line_width,
        }

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
        curve_drawer.set_axis_property(
            idx=idx,
            title=dataset_alias.upper(),
            x_label=x_label,
            y_label=y_label,
            x_ticks=x_ticks,
            y_ticks=y_ticks,
        )

        for method_name, method_setting in unique_method_settings.items():
            if method_name not in dataset_results:
                raise KeyError(f"{method_name} not in {sorted(dataset_results.keys())}")
            method_results = dataset_results[method_name]
            if mode == "pr":
                assert isinstance(method_results["p"], (list, tuple))
                assert isinstance(method_results["r"], (list, tuple))
                y_data = method_results["p"]
                x_data = method_results["r"]
            else:
                assert isinstance(method_results["fm"], (list, tuple))
                y_data = method_results["fm"]
                x_data = np.linspace(0, 1, 256)

            curve_drawer.plot_at_axis(
                idx=idx, method_curve_setting=method_setting, x_data=x_data, y_data=y_data
            )
    curve_drawer.save(path=save_name)
