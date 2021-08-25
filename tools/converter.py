# -*- coding: utf-8 -*-
# @Time    : 2021/8/25
# @Author  : Lart Pang
# @GitHub  : https://github.com/lartpang

import argparse
import importlib.util
import os
import sys
from itertools import chain

import numpy as np

parser = argparse.ArgumentParser(
    description="A useful and convenient tool to convert your .npy results into the table code in latex."
)
parser.add_argument(
    "-i", "--result-file", required=True, type=str, help="The path of the *_metrics.npy file."
)
parser.add_argument(
    "-o", "--tex-file", required=True, type=str, help="The path of the exported tex file."
)
parser.add_argument(
    "-c", "--config-file", type=str, help="The path of the customized config file."
)
parser.add_argument(
    "--contain-table-env",
    action="store_true",
    help="Whether to containe the table env in the exported code.",
)
args = parser.parse_args()


results = np.load(file=args.result_file, allow_pickle=True).item()
impossible_up_bound = 1
impossible_down_bound = 0

# 读取数据
dataset_names = sorted(list(results.keys()))
metric_names = ["SM", "wFm", "MAE", "adpF", "avgF", "maxF", "adpE", "avgE", "maxE"]
method_names = sorted(list(set(chain(*[list(results[n].keys()) for n in dataset_names]))))

if args.config_file is not None:
    assert args.config_file.endswith(".py")
    module_name = os.path.basename(args.config_file)
    spec = importlib.util.spec_from_file_location(module_name, args.config_file)
    module = importlib.util.module_from_spec(spec)
    if module_name in sys.modules:
        print(f"{module_name} has existed in sys.modules")
    else:
        sys.modules[module_name] = module
        print(f"{module_name} is loaded.")
    spec.loader.exec_module(module)
    if "dataset_names" not in module.__dict__:
        print(
            "`dataset_names` doesnot be contained in your config file, so we use the default config."
        )
    else:
        dataset_names = module.__dict__["dataset_names"]
    if "metric_names" not in module.__dict__:
        print(
            "`metric_names` doesnot be contained in your config file, so we use the default config."
        )
    else:
        metric_names = module.__dict__["metric_names"]
    if "method_names" not in module.__dict__:
        print(
            "`method_names` doesnot be contained in your config file, so we use the default config."
        )
    else:
        method_names = module.__dict__["method_names"]


print(
    f"CONFIG INFORMATION:\n - DATASETS: {dataset_names}]\n - METRICS: {metric_names}\n - METHODS: {method_names}"
)


# 整理表格
ori_column_list = []
column_list = []
for dataset_idx, dataset_name in enumerate(dataset_names):
    for metric_idx, metric_name in enumerate(metric_names):
        fiiled_value = (
            impossible_up_bound if metric_name.lower() == "mae" else impossible_down_bound
        )
        fiiled_dict = {k: fiiled_value for k in metric_names}
        ori_column = [
            results[dataset_name].get(method_name, fiiled_dict)[metric_name]
            for method_name in method_names
        ]
        column_list.append([x * round(1 - fiiled_value * 2) for x in ori_column])
        ori_column_list.append(ori_column)


style_templates = dict(
    method_column="{txt}",
    dataset_row_body="& \multicolumn{{{num_metrics}}}{{c}}{{\\textbf{{{dataset_name}}}}}",
    dataset_row_head=" ",
    metric_row_body="& {metric_name}",
    metric_row_head=" ",
    body=[
        "& {{\color{{reda}} \\textbf{{{txt:.03f}}}}}",  # top1
        "& {{\color{{mygreen}} \\textbf{{{txt:.03f}}}}}",  # top2
        "& {{\color{{myblue}} \\textbf{{{txt:.03f}}}}}",  # top3
        "& {txt:.03f}",  # other
    ],
)

# 排序并添加样式
def replace_cell(ori_value, k):
    if ori_value == impossible_up_bound or ori_value == impossible_down_bound:
        new_value = "& "
    else:
        new_value = style_templates["body"][k].format(txt=ori_value)
    return new_value


for col, ori_col in zip(column_list, ori_column_list):
    col_array = np.array(col).reshape(-1)
    sorted_col_array = np.sort(np.unique(col_array), axis=-1)
    # [top1_idxes, top2_idxes, top3_idxes]
    top_k_idxes = [np.argwhere(col_array == sorted_col_array[-i]).tolist() for i in range(1, 4)]
    for k, idxes in enumerate(top_k_idxes):
        for row_idx in idxes:
            ori_col[row_idx[0]] = replace_cell(ori_col[row_idx[0]], k)

    for idx, x in enumerate(ori_col):
        if not isinstance(x, str):
            ori_col[idx] = replace_cell(x, -1)


# 构建表头
num_metrics = len(metric_names)

dataset_row = (
    [style_templates["dataset_row_head"]]
    + [
        style_templates["dataset_row_body"].format(num_metrics=num_metrics, dataset_name=x)
        for x in dataset_names
    ]
    + [r"\\"]
)
metric_row = (
    [style_templates["metric_row_head"]]
    + [style_templates["metric_row_body"].format(metric_name=x) for x in metric_names]
    * len(dataset_names)
    + [r"\\"]
)

# 构建第一列
method_column = [style_templates["method_column"].format(txt=x) for x in method_names]
ori_column_list.insert(0, method_column)


if args.contain_table_env:
    column_style = "|".join([f"*{num_metrics}{{c}}"] * len(dataset_names))
    latex_table_head = [
        f"\\begin{{tabular}}{{l|{column_style}}}\n",
        "\\toprule[2pt]",
    ]
    latex_table_tail = [
        "\\bottomrule[2pt]\n",
        "\\end{tabular}",
    ]
else:
    latex_table_head = []
    latex_table_tail = []

row_list = (
    [latex_table_head, dataset_row, metric_row]
    + [row + (r"\\",) for row in zip(*ori_column_list)]
    + [latex_table_tail]
)

with open(args.tex_file, mode="w", encoding="utf-8") as f:
    for row in row_list:
        f.write("".join(row) + "\n")
