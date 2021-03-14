# -*- coding: utf-8 -*-

import os

from metrics.sod import cal_sod_matrics, draw_curves
from utils.generate_info import get_datasets_info, get_methods_info

"""
Include: Fm Curve/PR Curves/MAE/(max/mean/weighted) Fmeasure/Smeasure/Emeasure

NOTE:
* Our method automatically calculates the intersection of `pre` and `gt`.
    But it needs to have uniform naming rules for `pre` and `gt`.
"""

total_info = dict(
    rgb_sod=dict(
        dataset="/home/lart/Coding/Py-SOD-VOS-EvalToolkit/configs/datasets/json/rgb_sod.json",
        method="/home/lart/Coding/Py-SOD-VOS-EvalToolkit/configs/methods/json/rgb_sod_methods.json",
    ),
    rgb_cod=dict(
        dataset="/home/lart/Coding/Py-SOD-VOS-EvalToolkit/configs/datasets/json/rgb_cod.json",
        method="/home/lart/Coding/Py-SOD-VOS-EvalToolkit/configs/methods/json/rgb_cod_methods.json",
    ),
    rgbd_sod=dict(
        dataset="/home/lart/Coding/Py-SOD-VOS-EvalToolkit/configs/datasets/json/rgbd_sod.json",
        method="/home/lart/Coding/Py-SOD-VOS-EvalToolkit/configs/methods/json/rgbd_sod_methods.json",
    ),
)

for_pr = True  # 绘制pr曲线还是fm曲线

# 当前支持rgb_cod, rgb_sod, rgbd_sod
data_type = "rgb_cod"
data_info = total_info[data_type]

# 存放输出文件的文件夹
output_path = "./output"

# 包含所有待比较模型结果的信息和绘图配置的字典
dataset_info = get_datasets_info(datastes_info_json=data_info["dataset"])
drawing_info = get_methods_info(
    methods_info_json=data_info["method"], for_drawing=True, our_name="SINet"
)

# 用来保存测试结果的文件的路径
txt_path = os.path.join(output_path, f"{data_type}.txt")
xlsx_path = os.path.join(output_path, f"{data_type}.xlsx")

# 是否将评估结果到npy文件中，该文件可用来绘制pr和fm曲线
save_npy = True
# 保存曲线指标数据的文件路径
curves_npy_path = os.path.join(output_path, data_type + "_" + "curves.npy")
metrics_npy_path = os.path.join(output_path, data_type + "_" + "metrics.npy")

row_num = 1

# 不同曲线的绘图配置
axes_setting = {
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
        "y_lim": (0, 0.9),
    },
}
# 评估结果保留的小数点后数据的位数
num_bits = 3

# 是否保留之前的评估记录（针对txt_path文件有效）
resume_record = True

# 在计算指标的时候要跳过的数据集
skipped_datasets = []

cal_sod_matrics(
    data_type=data_type,
    txt_path=txt_path,
    resume_record=resume_record,
    xlsx_path=xlsx_path,
    drawing_info=drawing_info,
    dataset_info=dataset_info,
    skipped_datasets=skipped_datasets,
    save_npy=save_npy,
    curves_npy_path=curves_npy_path,
    metrics_npy_path=metrics_npy_path,
    num_bits=num_bits,
)

draw_curves(
    for_pr=for_pr,
    axes_setting=axes_setting,
    curves_npy_path=curves_npy_path,
    row_num=row_num,
    drawing_info=drawing_info,
    dataset_info=dataset_info,
)
