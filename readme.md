# 基于python的显著性目标检测测评工具箱

A Python-based salient object detection evaluation toolbox.

## TODO

- [ ] 添加更详细的注释
- [ ] 优化xlsx导出的代码
- [X] 剥离USVOS部分的代码，让本仓库更专注一些，相关代码已转移到另一个仓库[PyDavis16EvalToolbox](https://github.com/lartpang/PyDavis16EvalToolbox)。
- [ ] 提供对输出的结果基于某个指标进行排序的功能的支持（即，使表格更加直观）

## 重要提示

> 最近基于Fan的matlab代码，实现了一份更加快速和准确的指标代码<https://github.com/lartpang/PySODMetrics>，已经整合到该代码中。

- 2021年04月12日
    - 移除USVOS代码到独立的仓库。
    - 移动测试结果到<./results>中，日后会继续添加更多的模型的结果。
- 2021年03月21日
    - 正式删除需要个人定制的评估文件，这部分直接会放到本仓库的Readme中的[Examples](#Examples)中，仅供参考。
    - 将格式化输出功能调整，直接使用包`tabulate`处理，更加方便，输出的格式配置更丰富，详见<https://github.com/astanin/python-tabulate>
    - 调整原来`cal_sod_matrics`的`skipped_datasets`为:
      - `get_datasets_info`的`exclude_datasets/include_datasets`；
      - `get_methods_info`的`exclude_methods/include_methods`。
- 2021年03月14日
    - 这一版本将数据集和方法的配置方法转换为基于json文件的配置。
    - 一些配套的更改与简化。
- 2021年03月12日
    - 这一版本正式将sod的评估、绘图代码与配置分离，主要考虑如下
        - 用户的配置是需要调整的，这部分不适宜被git严格的监视，也便于提交后续更新的时候，直接忽略关于配置的更改，即后续更新时，
          用户配置部分会不再更新，若是添加新功能，直接调整原始的函数，其参数默认关闭新功能，保证用户不会受到影响。
        - sod和cosod评估方式有差异，但是绘图方式一致，所以现将评估绘图拆分成独立部分，置于metrics/sod文件夹下，之后或许或调整位置， 但这种拆分策略不变。
    - 优化了cosod的评估代码，对sod和cosod的指标recorder部分进行了简化。
    - 不再使用独立的sod_metrics代码，由于我已经将PySODMetrics发布到了PyPI上，所以可以直接通过pip安装。
    - 使用添加了对于print的一个彩色增强的封装，可见`./utils/misc.py`中的`colored_print`。
    - git不再跟踪方法配置文件和数据集配置文件，这部分现有的作为示例，仅供使用者独立补充和参考。
    - 修复了之前绘制Fm曲线时x的问题，之前取反了。详见<https://github.com/lartpang/Py-SOD-VOS-EvalToolkit/issues/2>。

## 特性

* 提供11项显著性目标检测指标的评估
    - F-measure-Threshold Curve
    - Precision-Recall Curve
    - MAE
    - weighted F-measure
    - S-measure
    - max/mean/adaptive F-measure
    - max/mean/adaptive E-measure
* 测试代码高度优化
    - 纯python实现，基于numpy和各种小trick计算各项指标，速度有保障
    - 导出特定模型的结果到xlsx文件中（2021年01月04日重新提供支持）
    - 导出测试结果到txt文件中
    - 评估所有指定的方法，根据评估结果绘制PR曲线和F-measure曲线

## 使用方法

### General/Co-RGB/RGBD-SOD

由于对于数据集和方法的配置因用户而异，所以在<https://github.com/lartpang/Py-SOD-VOS-EvalToolkit/commit/d7bcc1d74065844fe0483dc3ce3fda7d06d07bc0>
之后的版本不在更新`configs`文件夹中的这部分内容，直接给出一个简单的例子，用户可以自行修改。
例子可以参考之前的版本，例如：<https://github.com/lartpang/Py-SOD-VOS-EvalToolkit/tree/f9c1fd5ffeef1a58067e31b9e6d28e9eb0754c46/configs>

先安装指标代码库：

```python
pip install pysodmetrics
```

可见[Examples](#Examples)的配置注释。

## 最后

评估代码来自本人的另一个项目：<https://github.com/lartpang/PySODMetrics>，欢迎捉BUG！

## 编程参考

- Python_Openpyxl: <https://www.cnblogs.com/programmer-tlh/p/10461353.html>
- Python之re模块: <https://www.cnblogs.com/shenjianping/p/11647473.html>

## 结果汇总

详见 <./results> 下的各个文件。

## 相关文献

```text
@inproceedings{Fmeasure,
    title={Frequency-tuned salient region detection},
    author={Achanta, Radhakrishna and Hemami, Sheila and Estrada, Francisco and S{\"u}sstrunk, Sabine},
    booktitle=CVPR,
    number={CONF},
    pages={1597--1604},
    year={2009}
}

@inproceedings{MAE,
    title={Saliency filters: Contrast based filtering for salient region detection},
    author={Perazzi, Federico and Kr{\"a}henb{\"u}hl, Philipp and Pritch, Yael and Hornung, Alexander},
    booktitle=CVPR,
    pages={733--740},
    year={2012}
}

@inproceedings{Smeasure,
    title={Structure-measure: A new way to eval foreground maps},
    author={Fan, Deng-Ping and Cheng, Ming-Ming and Liu, Yun and Li, Tao and Borji, Ali},
    booktitle=ICCV,
    pages={4548--4557},
    year={2017}
}

@inproceedings{Emeasure,
    title="Enhanced-alignment Measure for Binary Foreground Map Evaluation",
    author="Deng-Ping {Fan} and Cheng {Gong} and Yang {Cao} and Bo {Ren} and Ming-Ming {Cheng} and Ali {Borji}",
    booktitle=IJCAI,
    pages="698--704",
    year={2018}
}

@inproceedings{wFmeasure,
  title={How to eval foreground maps?},
  author={Margolin, Ran and Zelnik-Manor, Lihi and Tal, Ayellet},
  booktitle=CVPR,
  pages={248--255},
  year={2014}
}
```

## Examples

<details>
<summary>
eval_cosod_all_methods.py
</summary>

```python
# -*- coding: utf-8 -*-
import os

from metrics.sod import cal_cosod_matrics, draw_curves
from utils.generate_info import get_datasets_info, get_methods_info

"""
Include: Fm Curve/PR Curves/MAE/(max/mean/weighted) Fmeasure/Smeasure/Emeasure

NOTE:
* Our method automatically calculates the intersection of `pre` and `gt`.
    But it needs to have uniform naming rules for `pre` and `gt`.
"""

total_info = dict(
    rgb_cosod=dict(
        dataset="/home/lart/Coding/Py-SOD-VOS-EvalToolkit/configs/datasets/json/rgb_cosod.json",
        method="/home/lart/Coding/Py-SOD-VOS-EvalToolkit/configs/methods/json/rgb_cosod_methods.json",
    ),
)

for_pr = True  # 是否绘制pr曲线

# 当前支持rgb_cosod
data_type = "rgb_cosod"
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

row_num = 2

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

cal_cosod_matrics(
    data_type=data_type,
    txt_path=txt_path,
    resume_record=resume_record,
    xlsx_path=xlsx_path,
    drawing_info=drawing_info,
    dataset_info=dataset_info,
    save_npy=save_npy,
    curves_npy_path=curves_npy_path,
    metrics_npy_path=metrics_npy_path,
    num_bits=num_bits,
)

draw_curves(
    for_pr=True,
    axes_setting=axes_setting,
    curves_npy_path=curves_npy_path,
    row_num=row_num,
    drawing_info=drawing_info,
    dataset_info=dataset_info,
)
```

</details>

<details>
<summary>
eval_sod_all_methods.py
</summary>

```python
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

for_drawing = False
for_pr = True  # 绘制pr曲线还是fm曲线

# 当前支持rgb_cod, rgb_sod, rgbd_sod
data_type = "rgbd_sod"
data_info = total_info[data_type]

# 存放输出文件的文件夹
output_path = "./output"

# 包含所有数据集信息的字典
dataset_info = get_datasets_info(
    datastes_info_json=data_info["dataset"],
    exclude_datasets=["STEREO797"],
)
# 包含所有待比较模型结果的信息和绘图配置的字典
drawing_info = get_methods_info(
    methods_info_json=data_info["method"],
    for_drawing=for_drawing,
    our_name="",
    exclude_methods=["UCNet_ABP", "UCNet_CVAE"],
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

cal_sod_matrics(
    data_type=data_type,
    txt_path=txt_path,
    resume_record=resume_record,
    xlsx_path=xlsx_path,
    drawing_info=drawing_info,
    dataset_info=dataset_info,
    save_npy=save_npy,
    curves_npy_path=curves_npy_path,
    metrics_npy_path=metrics_npy_path,
    num_bits=num_bits,
)

if for_drawing:
    draw_curves(
        for_pr=for_pr,
        axes_setting=axes_setting,
        curves_npy_path=curves_npy_path,
        row_num=row_num,
        drawing_info=drawing_info,
        dataset_info=dataset_info,
    )
```

</details>

<details>
<summary>
eval_sod_all_methods_from_mat.py
</summary>

```python
# -*- coding: utf-8 -*-
import os
from collections import defaultdict

import numpy as np
import scipy.io as scio

from metrics.sod import draw_curves
from utils.generate_info import get_datasets_info, get_methods_info
from utils.misc import colored_print, make_dir
from utils.print_formatter import print_formatter
from utils.recorders import MetricExcelRecorder, TxtRecorder

"""
This file can be used to plot curves with the 'mat' files from Fan's project:
- <https://github.com/DengPingFan/CODToolbox>

Include:
- Fm Curve,
- PR Curves,
- MAE,
- max/mean/adaptive/weighted F-measure,
- Smeasure,
- max/mean/adaptive Emeasure.

NOTE:
* Our method automatically calculates the intersection of `pre` and `gt`.
    But it needs to have uniform naming rules for `pre` and `gt`.
"""

total_info = dict(
    rgb_cosod=dict(
        dataset="/home/lart/Coding/Py-SOD-VOS-EvalToolkit/configs/datasets/json/rgb_cosod.json",
        method="/home/lart/Coding/Py-SOD-VOS-EvalToolkit/configs/methods/json/rgb_cosod_methods.json",
    ),
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


def export_valid_npy():
    """
    The function will save the results of all models on different datasets in a `npy` file in the
    form of a dictionary.
    {
      dataset1:{
        method1:[fm, em, p, r],
        method2:[fm, em, p, r],
        .....
      },
      dataset2:{
        method1:[fm, em, p, r],
        method2:[fm, em, p, r],
        .....
      },
      ....
    }
    """
    curves = defaultdict(dict)  # Two curve metrics
    metrics = defaultdict(dict)  # Six numerical metrics

    txt_recoder = TxtRecorder(
        txt_path=txt_path,
        resume=resume_record,
        max_method_name_width=max([len(x) for x in drawing_info.keys()]),  # 显示完整名字
    )
    excel_recorder = MetricExcelRecorder(
        xlsx_path=xlsx_path,
        sheet_name=data_type,
        row_header=["methods"],
        dataset_names=sorted(list(dataset_info.keys())),
        metric_names=["sm", "wfm", "mae", "adpf", "avgf", "maxf", "adpe", "avge", "maxe"],
    )

    for dataset_name in dataset_info.keys():
        # 使用dataset_name索引各个方法在不同数据集上的结果
        for method_name, method_info in drawing_info.items():
            method_result_path = method_info["path_dict"]

            # if dataset_name is None, `.get(dataset_name, other_value)` will return `other_value`.
            info_for_dataset = method_result_path.get(dataset_name, None)
            if info_for_dataset is None:
                colored_print(
                    msg=f"{method_name} does not have results on {dataset_name}", mode="warning"
                )
                continue

            mat_path = info_for_dataset.get("mat", None)
            if mat_path is None:
                colored_print(
                    msg=f"{method_name} does not have results on {dataset_name}", mode="warning"
                )
                continue

            method_result = scio.loadmat(mat_path)
            method_curves = {
                "p": method_result["column_Pr"].reshape(-1).round(num_bits).tolist(),
                "r": method_result["column_Rec"].reshape(-1).round(num_bits).tolist(),
                "fm": method_result["column_F"].reshape(-1).round(num_bits).tolist(),
            }
            method_metrics = {
                "maxF": method_result["maxFm"].reshape(-1).round(num_bits).item(),
                "avgF": method_result["meanFm"].reshape(-1).round(num_bits).item(),
                "adpF": method_result["adpFm"].reshape(-1).round(num_bits).item(),
                "maxE": method_result["maxEm"].reshape(-1).round(num_bits).item(),
                "avgE": method_result["meanEm"].reshape(-1).round(num_bits).item(),
                "adpE": method_result["adpEm"].reshape(-1).round(num_bits).item(),
                "wFm": method_result["wFm"].reshape(-1).round(num_bits).item(),
                "MAE": method_result["mae"].reshape(-1).round(num_bits).item(),
                "SM": method_result["Sm"].reshape(-1).round(num_bits).item(),
            }
            curves[dataset_name][method_name] = method_curves
            metrics[dataset_name][method_name] = method_metrics

            excel_recorder(
                row_data=method_metrics, dataset_name=dataset_name, method_name=method_name
            )
            txt_recoder(method_results=method_metrics, method_name=method_name)

    if save_npy:
        make_dir(os.path.dirname(curves_npy_path))
        np.save(curves_npy_path, curves)
        np.save(metrics_npy_path, metrics)
        colored_print(f"all methods have been saved in {curves_npy_path} and {metrics_npy_path}")
    formatted_string = print_formatter(metrics)
    colored_print(f"all methods have been tested:\n{formatted_string}")


if __name__ == "__main__":
    for_pr = True  # 绘制pr还是fm曲线

    data_type = "rgbd_sod"
    data_info = total_info[data_type]

    # 存放输出文件的文件夹
    output_path = "./output"

    # 包含所有待比较模型结果的信息和绘图配置的字典
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

    export_valid_npy()

    draw_curves(
        for_pr=for_pr,
        axes_setting=axes_setting,
        curves_npy_path=curves_npy_path,
        row_num=row_num,
        drawing_info=drawing_info,
        dataset_info=dataset_info,
    )
```

</details>

<details>
<summary>
eval_sod_single_method.py
</summary>

```python
# -*- coding: utf-8 -*-

import os

from tqdm import tqdm

from utils.generate_info import get_datasets_info
from utils.misc import colored_print, get_gt_pre_with_name, get_name_list, make_dir
from utils.print_formatter import print_formatter
from utils.recorders import MetricExcelRecorder, MetricRecorder

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


def cal_all_metrics():
    excel_recorder = MetricExcelRecorder(
        xlsx_path=xlsx_path,
        sheet_name=data_type,
        row_header=["methods"],
        dataset_names=sorted(list(dataset_info.keys())),
        metric_names=["sm", "wfm", "mae", "adpf", "avgf", "maxf", "adpe", "avge", "maxe"],
    )

    metrics = {}
    for dataset_name, dataset_path in dataset_info.items():
        if dataset_name in skipped_names:
            colored_print(msg=f"{dataset_name} will be skipped.", mode="warning")
            continue

        # 获取真值图片信息
        gt_info = dataset_path["mask"]
        gt_root = gt_info["path"]
        gt_ext = gt_info["suffix"]
        # 真值名字列表
        gt_index_file = dataset_path.get("index_file")
        if gt_index_file:
            gt_name_list = get_name_list(data_path=gt_index_file, file_ext=gt_ext)
        else:
            gt_name_list = get_name_list(data_path=gt_root, file_ext=gt_ext)
        assert len(gt_name_list) > 0, "there is not ground truth."

        # ==>> test the intersection between pre and gt for each method <<==
        method_dataset_info = pred_path.get(dataset_name, None)
        if method_dataset_info is None:
            colored_print(
                msg=f"{model_name} does not have results on {dataset_name}", mode="warning"
            )
            continue

        # 预测结果存放路径下的图片文件名字列表和扩展名称
        pre_ext = method_dataset_info["suffix"]
        pre_root = method_dataset_info["path"]
        pre_name_list = get_name_list(data_path=pre_root, file_ext=pre_ext)

        # get the intersection
        eval_name_list = sorted(list(set(gt_name_list).intersection(set(pre_name_list))))
        num_names = len(eval_name_list)

        if num_names == 0:
            colored_print(
                msg=f"{model_name} does not have results on {dataset_name}", mode="warning"
            )
            continue

        colored_print(
            f"Evaluating {model_name} with {len(eval_name_list)} images"
            f" (G:{len(gt_name_list)},P:{len(pre_name_list)}) images on dataset {dataset_name}"
        )

        metric_recoder = MetricRecorder()
        tqdm_bar = tqdm(
            eval_name_list, total=num_names, leave=False, ncols=119, desc=f"({dataset_name})"
        )
        for img_name in tqdm_bar:
            gt, pre = get_gt_pre_with_name(
                gt_root=gt_root,
                pre_root=pre_root,
                img_name=img_name,
                pre_ext=pre_ext,
                gt_ext=gt_ext,
                to_normalize=False,
            )
            metric_recoder.update(pre=pre, gt=gt)
        method_results = metric_recoder.show(num_bits=num_bits, return_ndarray=False)
        method_metrics = method_results["numerical"]
        metrics[dataset_name] = method_metrics

        excel_recorder(row_data=method_metrics, dataset_name=dataset_name, method_name=model_name)

        print(method_metrics)

    formatted_string = print_formatter(metrics)
    colored_print(f"all methods have been tested:\n{formatted_string}")


if __name__ == "__main__":
    data_type = "rgb_sod"
    data_info = total_info[data_type]
    output_path = "./output"  # 存放输出文件的文件夹
    make_dir(output_path)
    model_name = "CoNet"  # 待评估的模型名字
    pred_path = data_info["method"]["selecting"][model_name]  # 待评估的预测结果的路径
    # 包含所有待比较模型结果的信息和绘图配置的字典
    dataset_info = get_datasets_info(datastes_info_json=data_info["dataset"])
    export_xlsx = False  # 是否导出xlsx文件
    xlsx_path = os.path.join(output_path, "resutls.xlsx")  # xlsx文件的路径
    num_bits = 3  # 评估结果保留的小数点后数据的位数
    skipped_names = []  # 可以跳过指定的数据集
    cal_all_metrics()
```
</details>
