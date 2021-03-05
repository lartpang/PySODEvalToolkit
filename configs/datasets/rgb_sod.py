# -*- coding: utf-8 -*-
import os
from collections import OrderedDict

_RGB_SOD_ROOT = "/home/lart/Datasets/Saliency/RGBSOD"

ECSSD = dict(
    root=os.path.join(_RGB_SOD_ROOT, "ECSSD"),
    image=dict(path=os.path.join(_RGB_SOD_ROOT, "ECSSD", "Image"), suffix=".jpg"),
    mask=dict(path=os.path.join(_RGB_SOD_ROOT, "ECSSD", "Mask"), suffix=".png"),
)
DUTOMRON = dict(
    root=os.path.join(_RGB_SOD_ROOT, "DUT-OMRON"),
    image=dict(path=os.path.join(_RGB_SOD_ROOT, "DUT-OMRON", "Image"), suffix=".jpg"),
    mask=dict(path=os.path.join(_RGB_SOD_ROOT, "DUT-OMRON", "Mask"), suffix=".png"),
)
HKUIS = dict(
    root=os.path.join(_RGB_SOD_ROOT, "HKU-IS"),
    image=dict(path=os.path.join(_RGB_SOD_ROOT, "HKU-IS", "Image"), suffix=".png"),
    mask=dict(path=os.path.join(_RGB_SOD_ROOT, "HKU-IS", "Mask"), suffix=".png"),
)
PASCALS = dict(
    root=os.path.join(_RGB_SOD_ROOT, "PASCAL-S"),
    image=dict(path=os.path.join(_RGB_SOD_ROOT, "PASCAL-S", "Image"), suffix=".jpg"),
    mask=dict(path=os.path.join(_RGB_SOD_ROOT, "PASCAL-S", "Mask"), suffix=".png"),
)
SOC_TE = dict(
    root=os.path.join(_RGB_SOD_ROOT, "SOC/Test"),
    image=dict(path=os.path.join(_RGB_SOD_ROOT, "SOC/Test", "Image"), suffix=".jpg"),
    mask=dict(path=os.path.join(_RGB_SOD_ROOT, "SOC/Test", "Mask"), suffix=".png"),
)
DUTS_TE = dict(
    root=os.path.join(_RGB_SOD_ROOT, "DUTS/Test"),
    image=dict(path=os.path.join(_RGB_SOD_ROOT, "DUTS/Test", "Image"), suffix=".jpg"),
    mask=dict(path=os.path.join(_RGB_SOD_ROOT, "DUTS/Test", "Mask"), suffix=".png"),
)
DUTS_TR = dict(
    root=os.path.join(_RGB_SOD_ROOT, "DUTS/Train"),
    image=dict(path=os.path.join(_RGB_SOD_ROOT, "DUTS/Train", "Image"), suffix=".jpg"),
    mask=dict(path=os.path.join(_RGB_SOD_ROOT, "DUTS/Train", "Mask"), suffix=".png"),
)

rgb_sod_data = OrderedDict(
    {
        # "DUTS-TR": DUTS_TR,
        "PASCAL-S": PASCALS,
        "ECSSD": ECSSD,
        "HKU-IS": HKUIS,
        "DUT-OMRON": DUTOMRON,
        "DUTS-TE": DUTS_TE,
        "SOC": SOC_TE,
    }
)


def make_ax_info(pr_x_lim = None, pr_y_lim = None, fm_x_lim = None, fm_y_lim = None):
    default_info = {
        "pr": {  # pr曲线的配置
            "x_label": "Recall",  # 横坐标标签
            "y_label": "Precision",  # 纵坐标标签
            "x_lim": pr_x_lim or (0.1, 1),  # 横坐标显示范围
            "y_lim": pr_y_lim or (0.1, 1),  # 纵坐标显示范围
            },
        "fm": {  # fm曲线的配置
            "x_label": "Threshold",  # 横坐标标签
            "y_label": r"F$_{\beta}$",  # 纵坐标标签
            "x_lim": fm_x_lim or (0, 1),  # 横坐标显示范围
            "y_lim": fm_y_lim or (0, 1),  # 纵坐标显示范围
        },
    }
    return default_info
    

rgb_sod_info_for_drawing = OrderedDict(
    {
        # "DUTS-TR": DUTS_TR,
        "DUTS_TE": make_ax_info(fm_y_lim=(0.2, 0.9)),
        "PASCAL-S": make_ax_info(fm_y_lim=(0.3, 0.9)),
        "ECSSD": make_ax_info(fm_y_lim=(0.3, 1)),
        "HKU-IS": make_ax_info(fm_y_lim=(0.2, 1)),
        "DUT-OMRON": make_ax_info(fm_y_lim=(0.2, 0.8)),
        "SOC": make_ax_info(),
    }
)