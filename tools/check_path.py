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
        methods_info = json.load(f, object_pairs_hook=OrderedDict)  # 有序载入
    with open(dataset_json, encoding="utf-8", mode="r") as f:
        datasets_info = json.load(f, object_pairs_hook=OrderedDict)  # 有序载入

    total_msgs = []
    for method_name, method_info in methods_info.items():
        for dataset_name, resutls_info in method_info.items():
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
            else:
                pred_names = [
                    name[:-4] for name in os.listdir(dir_path) if name.endswith(file_suffix)
                ]
                if len(pred_names) == 0:
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
        print(f"{method_json} & {dataset_json} 基本正常")
