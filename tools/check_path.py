# -*- coding: utf-8 -*-

import argparse
import json
import os
from collections import OrderedDict

parser = argparse.ArgumentParser(description="A simple tool for checking your json config file.")
parser.add_argument(
    "-m", "--method-jsons", nargs="+", required=True, help="The json file about all methods."
)
parser.add_argument(
    "-d", "--dataset-jsons", nargs="+", required=True, help="The json file about all datasets."
)
args = parser.parse_args()

for method_json, dataset_json in zip(args.method_jsons, args.dataset_jsons):
    with open(method_json, encoding="utf-8", mode="r") as f:
        methods_info = json.load(f, object_hook=OrderedDict)  # 有序载入
    with open(dataset_json, encoding="utf-8", mode="r") as f:
        datasets_info = json.load(f, object_hook=OrderedDict)  # 有序载入

    total_msgs = []
    for method_name, method_info in methods_info.items():
        print(f"Checking for {method_name} ...")
        for dataset_name, results_info in method_info.items():
            if results_info is None:
                continue

            dataset_mask_info = datasets_info[dataset_name]["mask"]
            mask_path = dataset_mask_info["path"]
            mask_suffix = dataset_mask_info["suffix"]

            dir_path = results_info["path"]
            file_prefix = results_info.get("prefix", "")
            file_suffix = results_info["suffix"]

            if not os.path.exists(dir_path):
                total_msgs.append(f"{dir_path} 不存在")
                continue
            elif not os.path.isdir(dir_path):
                total_msgs.append(f"{dir_path} 不是正常的文件夹路径")
                continue
            else:
                pred_names = [
                    name[len(file_prefix) : -len(file_suffix)]
                    for name in os.listdir(dir_path)
                    if name.startswith(file_prefix) and name.endswith(file_suffix)
                ]
                if len(pred_names) == 0:
                    total_msgs.append(f"{dir_path} 中不包含前缀为{file_prefix}且后缀为{file_suffix}的文件")
                    continue

            mask_names = [
                name[: -len(mask_suffix)]
                for name in os.listdir(mask_path)
                if name.endswith(mask_suffix)
            ]
            intersection_names = set(mask_names).intersection(set(pred_names))
            if len(intersection_names) == 0:
                total_msgs.append(f"{dir_path} 中数据名字与真值 {mask_path} 不匹配")
            elif len(intersection_names) != len(mask_names):
                difference_names = set(mask_names).difference(pred_names)
                total_msgs.append(
                    f"{dir_path} 中数据({len(list(pred_names))})与真值({len(list(mask_names))})不一致"
                )

    if total_msgs:
        print(*total_msgs, sep="\n")
    else:
        print(f"{method_json} & {dataset_json} 基本正常")
