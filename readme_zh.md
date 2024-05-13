
# 基于 Python 的图像灰度/二值分割测评工具箱

## 一些规划

- 更灵活的配置脚本.
    - [ ] 使用 [符合matplotlib要求的](https://matplotlib.org/stable/tutorials/introductory/customizing.html#the-default-matplotlibrc-file) 的 yaml 文件来控制绘图格式.
    - [ ] 使用更加灵活的配置文件格式, 例如 yaml 或者 toml 替换 json.
- [ ] 添加测试脚本.
- [ ] 添加更详细的注释.
- 优化导出评估结果的代码.
    - [x] 实现导出结果到 XLSX 文件的代码.
    - [ ] 优化导出到 XLSX 文件的代码.
    - [ ] 是否应该使用 CSV 这样的文本格式更好些? 既可以当做文本文件打开, 亦可使用 Excel 来进行整理.
- [ ] 使用 `pathlib.Path` 替换 `os.path`.
- [x] 完善关于分组数据的代码, 即 CoSOD、Video Binary Segmentation 等任务的支持.
- [x] 支持并发策略加速计算. 目前保留了多线程支持, 剔除了之前的多进程代码.
    - [ ] 目前由于多线程的使用, 存在提示信息额外写入的问题, 有待优化.
- [X] 剥离 USVOS 代码到另一个仓库 [PyDavis16EvalToolbox](https://github.com/lartpang/PyDavis16EvalToolbox).
- [X] 使用更加快速和准确的指标代码 [PySODMetrics](https://github.com/lartpang/PySODMetrics) 作为评估基准.

> [!tip]
> - 一些方法提供的结果名字预原始数据集真值的名字不一致
>     - [注意] (2021-11-18) 当前同时提供了对名称前缀与后缀的支持, 所以基本不用用户自己改名字了.
>     - [可选] 可以使用提供的脚本 `tools/rename.py` 来批量修改文件名.**请小心使用, 以避免数据被覆盖.**
>     - [可选] 其他的工具: 例如 Linux 上的 `rename`, Windows 上的 [`Microsoft PowerToys`](https://github.com/microsoft/PowerToys)

## 特性

- 受益于 PySODMetrics, 从而获得了更加丰富的指标的支持. 更多细节可见 `utils/recorders/metric_recorder.py`.
    - 支持评估*灰度图像*, 例如来自显著性目标检测任务的预测.
        - MAE
        - Emeasure
        - Smeasure
        - Weighted Fmeasure
        - Maximum/Average/Adaptive Fmeasure
        - Maximum/Average/Adaptive Precision
        - Maximum/Average/Adaptive Recall
        - Maximum/Average/Adaptive IoU
        - Maximum/Average/Adaptive Dice
        - Maximum/Average/Adaptive Specificity
        - Maximum/Average/Adaptive BER
        - Fmeasure-Threshold Curve (执行 `eval.py` 请指定指标 `fmeasure`)
        - Emeasure-Threshold Curve (执行 `eval.py` 请指定指标 `em`)
        - Precision-Recall Curve (执行 `eval.py` 请指定指标 `precision` 和 `recall`，这一点不同于以前的版本，因为 `precision` 和 `recall` 的计算被从 `fmeasure` 中独立出来了)
    - 支持评估*二值图像*, 例如常见的二值分割任务.
        - Binary Fmeasure
        - Binary Precision
        - Binary Recall
        - Binary IoU
        - Binary Dice
        - Binary Specificity
        - Binary BER
- 更丰富的功能.
    - 支持根据配置评估模型.
    - 支持根据配置和评估结果绘制 PR 曲线和 F-measure 曲线.
    - 支持导出结果到 TXT 文件中.
    - 支持导出结果到 XLSX 文件 (2021 年 01 月 04 日重新提供支持).
    - 支持从生成的 `.npy` 文件导出 LaTeX 表格代码, 同时支持对最优的前三个方法用不同颜色进行标记.
    - … :>.

## 使用方法

### 安装依赖

安装相关依赖库: `pip install -r requirements.txt` .

其中指标库是我的另一个项目: [PySODMetrics](https://github.com/lartpang/PySODMetrics), 欢迎捉 BUG!

### 配置数据集与方法预测的路径信息

本项目依赖于 json 文件存放数据, `./examples` 中已经提供了数据集和方法配置的例子: `config_dataset_json_example.json` 和 `config_method_json_example.json` , 可以至直接修改他们用于后续步骤.

> [!note]
> - 请注意, 由于本项目依赖于 OpenCV 读取图片, 所以请确保路径字符串不包含非 ASCII 字符.
> - 请务必确保*数据集配置文件中数据集的名字*和*方法配置文件中数据集的名字*一致. 准备好 json 文件后, 建议使用提供的 `tools/check_path.py` 来检查下 json 文件中的路径信息是否正常.

<details>
<summary>
关于配置的更多细节
</summary>

例子 1: 数据集配置

注意, 这里的 "image" 并不是必要的. 实际评估仅仅读取 "mask".

```json
{
    "LFSD": {
        "image": {
            "path": "Path_Of_RGBDSOD_Datasets/LFSD/Image",
            "prefix": "some_gt_prefix",
            "suffix": ".jpg"
        },
        "mask": {
            "path": "Path_Of_RGBDSOD_Datasets/LFSD/Mask",
            "prefix": "some_gt_prefix",
            "suffix": ".png"
        }
    }
}
```

例子 2: 方法配置

```json
{
    "Method1": {
        "PASCAL-S": {
            "path": "Path_Of_Method1/PASCAL-S",
            "prefix": "some_method_prefix",
            "suffix": ".png"
        },
        "ECSSD": {
            "path": "Path_Of_Method1/ECSSD",
            "prefix": "some_method_prefix",
            "suffix": ".png"
        },
        "HKU-IS": {
            "path": "Path_Of_Method1/HKU-IS",
            "prefix": "some_method_prefix",
            "suffix": ".png"
        },
        "DUT-OMRON": {
            "path": "Path_Of_Method1/DUT-OMRON",
            "prefix": "some_method_prefix",
            "suffix": ".png"
        },
        "DUTS-TE": {
            "path": "Path_Of_Method1/DUTS-TE",
            "suffix": ".png"
        }
    }
}
```

这里 `path` 表示存放图像数据的目录. 而 `prefix` 和 `suffix` 表示实际预测图像和真值图像*名字中除去共有部分外*的前缀预后缀内容.

评估过程中, 方法预测和数据集真值匹配的方式是基于文件名字的共有部分. 二者的名字模式预设为 `[prefix]+[shared-string]+[suffix]` . 例如假如有这样的预测图像 `method1_00001.jpg` , `method1_00002.jpg` , `method1_00003.jpg` 和真值图像 `gt_00001.png` , `gt_00002.png` , `gt_00003.png` . 则我们可以配置如下:

例子 3: 数据集配置

```json
{
    "dataset1": {
        "mask": {
            "path": "path/Mask",
            "prefix": "gt_",
            "suffix": ".png"
        }
    }
}
```

例子 4: 方法配置

```json
{
    "method1": {
        "dataset1": {
            "path": "path/dataset1",
            "prefix": "method1_",
            "suffix": ".jpg"
        }
    }
}
```

</details>

### 执行评估过程

- 前述步骤一切正常后, 可以开始评估了. 评估脚本用法可参考命令 `python eval.py --help` 的输出.
- 根据自己需求添加配置项并执行即可. 如无异常, 会生成指定文件名的结果文件.
  - 如果不指定所有的文件, 那么就直接输出结果, 具体可见 `eval.py` 的帮助信息.
  - 如指定 `--curves-npy`, 绘图相关的指标信息将会保存到对应的 `.npy` 文件中.
- [可选] 可以使用 `tools/converter.py` 直接从生成的 npy 文件中导出 latex 表格代码.

### 为灰度图像的评估绘制曲线

可以使用 `plot.py` 来读取 `.npy` 文件按需对指定方法和数据集的结果整理并绘制 `PR` , `F-measure` 和 `E-measure` 曲线. 该脚本用法可见 `python plot.py --help` 的输出. 按照自己需求添加配置项并执行即可.

最基本的一条是请按照子图数量, 合理地指定配置文件中的 `figure.figsize` 项的数值.

### 一个基本的执行流程

这里以我自己本地的 configs 文件夹中的 RGB SOD 的配置 (需要根据实际情况进行必要的修改) 为例.

```shell
# 检查配置文件
python tools/check_path.py --method-jsons configs/methods/rgb-sod/rgb_sod_methods.json --dataset-jsons configs/datasets/rgb_sod.json

# 在输出信息中没有不合理的地方后，开始进行评估
# --dataset-json 数据集配置文件 configs/datasets/rgb_sod.json
# --method-json 方法配置文件 configs/methods/rgb-sod/rgb_sod_methods.json
# --metric-npy 输出评估结果数据到 output/rgb_sod/metrics.npy
# --curves-npy 输出曲线数据到 output/rgb_sod/curves.npy
# --record-txt 输出评估结果文本到 output/rgb_sod/results.txt
# --record-xlsx 输出评估结果到excel文档 output/rgb_sod/results.xlsx
# --metric-names 所有结果仅包含给定指标的信息, 涉及到曲线的四个指标分别为 fmeasure em precision recall
# --include-methods 评估过程仅包含 configs/methods/rgb-sod/rgb_sod_methods.json 中的给定方法
# --include-datasets 评估过程仅包含 configs/datasets/rgb_sod.json 中的给定数据集
python eval.py --dataset-json configs/datasets/rgb_sod.json --method-json configs/methods/rgb-sod/rgb_sod_methods.json --metric-npy output/rgb_sod/metrics.npy --curves-npy output/rgb_sod/curves.npy --record-txt output/rgb_sod/results.txt --record-xlsx output/rgb_sod/results.xlsx --metric-names sm wfm mae fmeasure em precision recall --include-methods MINet_R50_2020 GateNet_2020 --include-datasets PASCAL-S ECSSD

# 得到曲线数据文件，即这里的 output/rgb_sod/curves.npy 文件后，就可以开始绘制图像了

# 简单的例子，下面指令执行后，结果保存为 output/rgb_sod/simple_curve_pr.pdf
# --style-cfg 使用图像风格配置文件 examples/single_row_style.yml，这里子图较少，直接使用单行的配置
# --num-rows 图像子图都位于一行
# --curves-npys 将使用曲线数据文件 output/rgb_sod/curves.npy 来绘图
# --mode pr: 绘制是pr曲线；fm: 绘制的是fm曲线
# --save-name 图像保存路径，只需写出名字，代码会加上由前面指定的 --style-cfg 中的 `savefig.format` 项指定的格式后缀名
# --alias-yaml: 使用 yaml 文件指定绘图中使用的方法别名和数据集别名
python plot.py --style-cfg examples/single_row_style.yml --num-rows 1 --curves-npys output/rgb_sod/curves.npy --mode pr --save-name output/rgb_sod/simple_curve_pr --alias-yaml configs/rgb_aliases.yaml

# 复杂的例子，下面指令执行后，结果保存为 output/rgb_sod/complex_curve_pr.pdf

# --style-cfg 使用图像风格配置文件 examples/single_row_style.yml，这里子图较少，直接使用单行的配置
# --num-rows 图像子图都位于一行
# --curves-npys 将使用曲线数据文件 output/rgb_sod/curves.npy 来绘图
# --our-methods 在图中使用红色实线加粗标注指定的方法 MINet_R50_2020
# --num-col-legend 图像子图图示中信息的列数
# --mode pr: 绘制是pr曲线；fm: 绘制的是fm曲线
# --separated-legend 使用共享的单个图示
# --sharey 使用共享的 y 轴刻度，这将仅在每行的第一个图上显示刻度值
# --save-name 图像保存路径，只需写出名字，代码会加上由前面指定的 --style-cfg 中的 `savefig.format` 项指定的格式后缀名
python plot.py --style-cfg examples/single_row_style.yml --num-rows 1 --curves-npys output/rgb_sod/curves.npy --our-methods MINet_R50_2020 --num-col-legend 1 --mode pr --separated-legend --sharey --save-name output/rgb_sod/complex_curve_pr
```

## 绘图示例

**Precision-Recall Curve**:

![PRCurves](https://user-images.githubusercontent.com/26847524/227249768-a41ef076-6355-4b96-a291-fc0e071d9d35.jpg)

**F-measure Curve**:

![fm-curves](https://user-images.githubusercontent.com/26847524/227249746-f61d7540-bb73-464d-bccf-9a36323dec47.jpg)

**E-measure Curve**:

![em-curves](https://user-images.githubusercontent.com/26847524/227249727-8323d5cf-ddd7-427b-8152-b8f47781c4e3.jpg)

## 编程参考

- `openpyxl` 库: <https://www.cnblogs.com/programmer-tlh/p/10461353.html>
- `re` 模块: <https://www.cnblogs.com/shenjianping/p/11647473.html>

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
