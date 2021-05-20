# -*- coding: utf-8 -*-
import os

from metrics import draw_curves
from utils.generate_info import get_datasets_info, get_methods_info
from utils.misc import make_dir

"""
Include: Fm Curve/PR Curves/MAE/(max/mean/weighted) Fmeasure/Smeasure/Emeasure

NOTE:
* Our method automatically calculates the intersection of `pre` and `gt`.
    But it needs to have uniform naming rules for `pre` and `gt`.
"""

total_info = dict(
    rgb_sod=dict(
        dataset="/home/lart/Coding/GIT/PySODEvalToolkit/configs/datasets/json/rgb_sod.json",
        method="/home/lart/Coding/GIT/PySODEvalToolkit/configs/methods/json/rgb_sod_methods.json",
    ),
    rgb_cod=dict(
        dataset="/home/lart/Coding/GIT/PySODEvalToolkit/configs/datasets/json/rgb_cod.json",
        method="/home/lart/Coding/GIT/PySODEvalToolkit/configs/methods/json/rgb_cod_methods.json",
    ),
    rgbd_sod=dict(
        dataset="/home/lart/Coding/GIT/PySODEvalToolkit/configs/datasets/json/rgbd_sod.json",
        method="/home/lart/Coding/GIT/PySODEvalToolkit/configs/methods/json/rgbd_sod_methods_ablation.json",
    ),
)

# 当前支持rgb_cod, rgb_sod, rgbd_sod
data_type = "rgbd_sod"
data_info = total_info[data_type]

# 存放输出文件的文件夹
output_path = "../output"
make_dir(output_path)

# 包含所有数据集信息的字典
dataset_info = get_datasets_info(
    datastes_info_json=data_info["dataset"],
    # include_datasets=["NJUD"],
    exclude_datasets=["LFSD"],
)
# 包含所有待比较模型结果的信息和绘图配置的字典
drawing_info = get_methods_info(
    methods_info_json=data_info["method"],
    for_drawing=True,
    our_name="Ours",
    # include_methods=["CTMF_V16"],
    # exclude_methods=["UCNet_ABP"],
)

# 保存曲线指标数据的文件路径
curves_npy_path = os.path.join(output_path, data_type + "_" + "curves.npy")

# json中存储的方法名字并不是我实际想要用来作为图例的名字，这里需要修改line_label
new_drawing_info = []
for method_name, method_info in drawing_info.items():
    label_name = method_info["curve_setting"]["line_label"]
    label_name = label_name.split("_")[0]
    method_info["curve_setting"]["line_label"] = label_name

draw_curves.draw_curves(
    for_pr=False,
    # 不同曲线的绘图配置
    axes_setting={
        # pr曲线的配置
        "pr": {
            # 横坐标标签
            "x_label": "Recall",
            # 纵坐标标签
            "y_label": "Precision",
            # 横坐标显示范围
            "x_lim": (0.1, 1),
            # 纵坐标显示范围
            "y_lim": (0.1, 1),
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
            "y_lim": (0, 1),
        },
    },
    curves_npy_path=curves_npy_path,
    row_num=1,
    drawing_info=drawing_info,
    dataset_info=dataset_info,
    dataset_alias={  # 将dataset json中的名字替换为想要显示的名字
        "DUTRGBD": "DUTRGBD",
        "STEREO1000": "SETERE",
    },
)
