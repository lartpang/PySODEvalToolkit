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
    "-i",
    "--result-file",
    required=True,
    nargs="+",
    action="extend",
    help="The path of the *_metrics.npy file.",
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
parser.add_argument(
    "--transpose",
    action="store_true",
    help="Whether to transpose the table.",
)
args = parser.parse_args()


def update_dict(parent_dict, sub_dict):
    for sub_k, sub_v in sub_dict.items():
        if sub_k in parent_dict:
            if sub_v is not None and isinstance(sub_v, dict):
                update_dict(parent_dict=parent_dict[sub_k], sub_dict=sub_v)
                continue
        parent_dict.update(sub_dict)


results = {}
for result_file in args.result_file:
    result = np.load(file=result_file, allow_pickle=True).item()
    update_dict(results, result)

IMPOSSIBLE_UP_BOUND = 1
IMPOSSIBLE_DOWN_BOUND = 0

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
    f"CONFIG INFORMATION:"
    f"\n- DATASETS ({len(dataset_names)}): {dataset_names}]"
    f"\n- METRICS ({len(metric_names)}): {metric_names}"
    f"\n- METHODS ({len(method_names)}): {method_names}"
)

if isinstance(metric_names, (list, tuple)):
    ori_metric_names = metric_names
elif isinstance(metric_names, dict):
    ori_metric_names, metric_names = list(zip(*list(metric_names.items())))
else:
    raise NotImplementedError

if isinstance(method_names, (list, tuple)):
    ori_method_names = method_names
elif isinstance(method_names, dict):
    ori_method_names, method_names = list(zip(*list(method_names.items())))
else:
    raise NotImplementedError

# 整理表格
ori_columns = []
column_for_index = []
for dataset_idx, dataset_name in enumerate(dataset_names):
    for metric_idx, ori_metric_name in enumerate(ori_metric_names):
        fiiled_value = (
            IMPOSSIBLE_UP_BOUND if ori_metric_name.lower() == "mae" else IMPOSSIBLE_DOWN_BOUND
        )
        fiiled_dict = {k: fiiled_value for k in ori_metric_names}
        ori_column = [
            results[dataset_name].get(method_name, fiiled_dict)[ori_metric_name]
            for method_name in ori_method_names
        ]
        column_for_index.append([x * round(1 - fiiled_value * 2) for x in ori_column])
        ori_columns.append(ori_column)

style_templates = dict(
    method_row_body="& {method_name}",
    method_column_body=" {method_name}",
    dataset_row_body="& \multicolumn{{{num_metrics}}}{{c}}{{\\textbf{{{dataset_name}}}}}",
    dataset_column_body="\multirow{{-{num_metrics}}}{{*}}{{\\rotatebox{{90}}{{\\textbf{{{dataset_name}}}}}}}",
    dataset_head=" ",
    metric_body="& {metric_name}",
    metric_row_head=" ",
    metric_column_head="& ",
    body=[
        "& {{\color{{reda}} \\textbf{{{txt:.03f}}}}}",  # top1
        "& {{\color{{mygreen}} \\textbf{{{txt:.03f}}}}}",  # top2
        "& {{\color{{myblue}} \\textbf{{{txt:.03f}}}}}",  # top3
        "& {txt:.03f}",  # other
    ],
)


# 排序并添加样式
def replace_cell(ori_value, k):
    if ori_value == IMPOSSIBLE_UP_BOUND or ori_value == IMPOSSIBLE_DOWN_BOUND:
        new_value = "& "
    else:
        new_value = style_templates["body"][k].format(txt=ori_value)
    return new_value


for col, ori_col in zip(column_for_index, ori_columns):
    col_array = np.array(col).reshape(-1)
    sorted_col_array = np.sort(np.unique(col_array), axis=-1)[-3:][::-1]
    # [top1_idxes, top2_idxes, top3_idxes]
    top_k_idxes = [np.argwhere(col_array == x).tolist() for x in sorted_col_array]
    for k, idxes in enumerate(top_k_idxes):
        for row_idx in idxes:
            ori_col[row_idx[0]] = replace_cell(ori_col[row_idx[0]], k)

    for idx, x in enumerate(ori_col):
        if not isinstance(x, str):
            ori_col[idx] = replace_cell(x, -1)

# 构建表头
num_datasets = len(dataset_names)
num_metrics = len(metric_names)
num_methods = len(method_names)

# 先构开头的列，再整体构造开头的行
latex_table_head = []
latex_table_tail = []

if not args.transpose:
    dataset_row = (
        [style_templates["dataset_head"]]
        + [
            style_templates["dataset_row_body"].format(num_metrics=num_metrics, dataset_name=x)
            for x in dataset_names
        ]
        + [r"\\"]
    )
    metric_row = (
        [style_templates["metric_row_head"]]
        + [style_templates["metric_body"].format(metric_name=x) for x in metric_names]
        * num_datasets
        + [r"\\"]
    )
    additional_rows = [dataset_row, metric_row]

    # 构建第一列
    method_column = [
        style_templates["method_column_body"].format(method_name=x) for x in method_names
    ]
    additional_columns = [method_column]

    columns = additional_columns + ori_columns
    rows = [list(row) + [r"\\"] for row in zip(*columns)]
    rows = additional_rows + rows

    if args.contain_table_env:
        column_style = "|".join([f"*{num_metrics}{{c}}"] * len(dataset_names))
        latex_table_head = [
            f"\\begin{{tabular}}{{l|{column_style}}}\n",
            "\\toprule[2pt]",
        ]
else:
    dataset_column = []
    for x in dataset_names:
        blank_cells = [" "] * (num_metrics - 1)
        dataset_cell = [
            style_templates["dataset_column_body"].format(num_metrics=num_metrics, dataset_name=x)
        ]
        dataset_column.extend(blank_cells + dataset_cell)
    metric_column = [
        style_templates["metric_body"].format(metric_name=x) for x in metric_names
    ] * num_datasets
    additional_columns = [dataset_column, metric_column]

    method_row = (
        [style_templates["dataset_head"], style_templates["metric_column_head"]]
        + [style_templates["method_row_body"].format(method_name=x) for x in method_names]
        + [r"\\"]
    )
    additional_rows = [method_row]

    additional_columns = [list(x) for x in zip(*additional_columns)]
    rows = [cells + row + [r"\\"] for cells, row in zip(additional_columns, ori_columns)]
    rows = additional_rows + rows

    if args.contain_table_env:
        column_style = "".join([f"*{{{num_methods}}}{{c}}"])
        latex_table_head = [
            f"\\begin{{tabular}}{{cc|{column_style}}}\n",
            "\\toprule[2pt]",
        ]

if args.contain_table_env:
    latex_table_tail = [
        "\\bottomrule[2pt]\n",
        "\\end{tabular}",
    ]

rows = [latex_table_head] + rows + [latex_table_tail]

with open(args.tex_file, mode="w", encoding="utf-8") as f:
    for row in rows:
        f.write("".join(row) + "\n")
