# -*- coding: utf-8 -*-

import math

import numpy as np

from utils.misc import colored_print
from utils.recorders import CurveDrawer


def draw_curves(
    for_pr: bool = True,
    axes_setting: dict = None,
    curves_npy_path: str = "",
    row_num: int = 1,
    drawing_info: dict = None,
    dataset_info: dict = None,
    dataset_alias: dict = None,
    font_cfg: dict = None,
    subplots_cfg: dict = None,
    separated_legend: bool = False,
    sharey: bool = False,
):
    if dataset_alias is None:
        dataset_alias = {}

    if drawing_info is None or not isinstance(drawing_info, dict) or len(drawing_info.keys()) == 0:
        raise ValueError("drawing_info must contain valid information about the results.")

    if dataset_info is None or not isinstance(dataset_info, dict) or len(dataset_info.keys()) == 0:
        raise ValueError("dataset_info must contain valid information about the datasets.")

    mode = "pr" if for_pr else "fm"
    mode_axes_setting = axes_setting[mode]

    x_label, y_label = mode_axes_setting["x_label"], mode_axes_setting["y_label"]
    x_lim, y_lim = mode_axes_setting["x_lim"], mode_axes_setting["y_lim"]

    curves = np.load(curves_npy_path, allow_pickle=True).item()

    curve_drawer = CurveDrawer(
        row_num=row_num,
        num_subplots=len(dataset_info.keys()),
        font_cfg=font_cfg,
        subplots_cfg=subplots_cfg,
        separated_legend=separated_legend,
        sharey=sharey,
    )

    for idx, dataset_name in enumerate(dataset_info.keys()):
        # 与cfg[dataset_info]中的key保持一致
        dataset_results = curves[dataset_name]
        curve_drawer.set_axis_property(
            idx=idx,
            title=dataset_alias.get(dataset_name, dataset_name).upper(),
            x_label=x_label,
            y_label=y_label,
            x_lim=x_lim,
            y_lim=y_lim,
        )

        for method_name, method_info in drawing_info.items():
            # 与cfg[drawing_info]中的key保持一致
            method_results = dataset_results.get(method_name, None)
            if method_results is None:
                colored_print(
                    msg=f"{method_name} does not have results on {dataset_name}", mode="warning"
                )
                continue

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
                idx=idx,
                method_curve_setting=method_info["curve_setting"],
                x_data=x_data,
                y_data=y_data,
            )
    curve_drawer.show()
