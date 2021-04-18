# -*- coding: utf-8 -*-

import json
import os
from collections import OrderedDict

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
        method="/home/lart/Coding/GIT/PySODEvalToolkit/configs/methods/json/rgbd_sod_methods.json",
    ),
)


exclude_json = ["rgb_sod", "rgb_cod"]
exclude_dataset = []
exclude_method = []

for data_type, json_info in total_info.items():
    if data_type in exclude_json:
        continue

    with open(json_info["method"], encoding="utf-8", mode="r") as f:
        methods_info = json.load(f, object_pairs_hook=OrderedDict)  # 有序载入
    with open(json_info["dataset"], encoding="utf-8", mode="r") as f:
        datasets_info = json.load(f, object_pairs_hook=OrderedDict)  # 有序载入

    total_msgs = []
    for method_name, method_info in methods_info.items():
        if method_name in exclude_dataset:
            continue
        for dataset_name, resutls_info in method_info.items():
            if dataset_name in exclude_method:
                continue
            if resutls_info is None:
                continue

            dataset_mask_info = datasets_info[dataset_name]["mask"]
            mask_path = dataset_mask_info["path"]
            mask_suffix = dataset_mask_info["suffix"]

            dir_path = resutls_info["path"]
            file_suffix = resutls_info["suffix"]

            if not os.path.exists(dir_path):
                total_msgs.append(f"{method_name}/{dataset_name}: {dir_path} 不存在")
                continue
            elif not os.path.isdir(dir_path):
                total_msgs.append(f"{method_name}/{dataset_name}: {dir_path} 不是正常的文件夹路径")
                continue
            elif (
                len(
                    pred_names := [
                        name[:-4] for name in os.listdir(dir_path) if name.endswith(file_suffix)
                    ]
                )
                == 0
            ):
                total_msgs.append(
                    f"{method_name}/{dataset_name}: {dir_path} 中不包含后缀为{file_suffix}的文件"
                )
                continue

            mask_names = [
                name[:-4] for name in os.listdir(mask_path) if name.endswith(mask_suffix)
            ]
            if len(set(mask_names).intersection(set(pred_names))) == 0:
                total_msgs.append(
                    f"{method_name}/{dataset_name}: {dir_path} 中数据名字与真值 {mask_path} 不匹配"
                )

    if total_msgs:
        print(*total_msgs, sep="\n")
    else:
        print(f"{data_type} 基本正常")
