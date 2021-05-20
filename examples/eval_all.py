# -*- coding: utf-8 -*-
import os

from metrics import cal_sod_matrics
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
    include_datasets=["NJUD"],
    # exclude_datasets=["LFSD"],
)
# 包含所有待比较模型结果的信息和绘图配置的字典
drawing_info = get_methods_info(
    methods_info_json=data_info["method"],
    for_drawing=True,
    our_name="",
    include_methods=["CTMF_V16"],
    # exclude_methods=["UCNet_ABP", "UCNet_CVAE"],
)

cal_sod_matrics.cal_sod_matrics(
    data_type=data_type,
    resume_record=True,  # 是否保留之前的评估记录（针对txt_path文件有效）
    txt_path=os.path.join(output_path, f"{data_type}.txt"),
    xlsx_path=os.path.join(output_path, f"other_{data_type}.xlsx"),
    drawing_info=drawing_info,
    dataset_info=dataset_info,
    save_npy=True,  # 是否将评估结果到npy文件中，该文件可用来绘制pr和fm曲线
    # 保存曲线指标数据的文件路径
    curves_npy_path=os.path.join(output_path, data_type + "_" + "curves.npy"),
    metrics_npy_path=os.path.join(output_path, data_type + "_" + "metrics.npy"),
    num_bits=3,  # 评估结果保留的小数点后数据的位数
)
