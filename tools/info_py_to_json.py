# -*- coding: utf-8 -*-
# @Time    : 2021/3/14
# @Author  : Lart Pang
# @GitHub  : https://github.com/lartpang
import json
import os
import sys
from importlib import import_module

from mmcv import Config

source_config_root = "../configs/datasets/py"
sys.path.insert(0, source_config_root)

source_config_files = os.listdir(source_config_root)
for source_config_file in source_config_files:
    source_config_path = os.path.join(source_config_root, source_config_file)
    if not os.path.isfile(source_config_path):
        continue
    print(source_config_path)
    temp_module_name = os.path.splitext(source_config_file)[0]
    Config._validate_py_syntax(source_config_path)
    mod = import_module(temp_module_name)

    total_dict = {}
    for name, value in mod.__dict__.items():
        name: str
        # For Methods
        # if not name.startswith("_") and isinstance(value, dict):
        #     total_dict[name] = value

        # For Datasets
        if not name.startswith("_") and name.endswith("_data") and isinstance(value, dict):
            total_dict = value

    # delete imported module
    del sys.modules[temp_module_name]

    with open(
        f"../datasets/json/{os.path.basename(temp_module_name)}.json", encoding="utf-8", mode="w"
    ) as f:
        json.dump(total_dict, f, indent=2)
