# 基于Python的图像二值分割测评工具箱

A Python-based image binary segmentation evaluation toolbox.

基于Python的图像二值分割测评工具箱

## 一些规划

* [ ] 向执行脚本中添加配置信息合理行检测.
* 更灵活的配置脚本.
  + [ ] 使用[符合matplotlib要求的](https://matplotlib.org/stable/tutorials/introductory/customizing.html#the-default-matplotlibrc-file)的 yaml 文件来控制绘图格式.
  + [ ] 是否应该使用更加灵活强大的配置格式, 例如 yaml 或者 toml 来替换配置策略.
* [ ] 添加测试脚本.
* [ ] 添加更详细的注释.
* 优化导出评估结果的代码.
  + [x] 实现导出 XLSX 文件的代码.
  + [ ] 优化导出到 XLSX 文件的代码.
  + [ ] 是否应该使用 CSV 这样的文本格式更好些? 既可以当做文本文件打开, 亦可使用Excel来进行整理.
* [ ] 使用 `pathlib.Path` 替换 `os.path`.
* [ ] 完善关于分组数据的代码, 即 CoSOD、Video Binary Segmentation 等任务的支持.
* [x] 支持并发策略加速计算. 目前保留了多线程支持, 剔除了之前的多进程代码.
* [X] 剥离 USVOS 代码到另一个仓库 [PyDavis16EvalToolbox](https://github.com/lartpang/PyDavis16EvalToolbox).
* [X] 基于 github page 服务自动化生成结果汇总网页, 并支持基于某个指标进行排序的支持.
* [X] 使用更加快速和准确的指标代码 [PySODMetrics](https://github.com/lartpang/PySODMetrics) 作为评估基准.

## 特性

* 受益于 PySODMetrics, 从而获得了更加丰富的指标的支持. 更多细节可见 `utils/recorders/metric_recorder.py`.
  + 支持评估*灰度图像*, 例如来自显著性目标检测任务的预测.
    - MAE
    - Emeasure
    - Smeasure
    - weighted Fmeasure
    - maximum/average/adaptive Fmeasure
    - maximum/average/adaptive Precision
    - maximum/average/adaptive Recall
    - maximum/average/adaptive IoU
    - maximum/average/adaptive Dice
    - maximum/average/adaptive Specificity
    - maximum/average/adaptive BER
    - Fmeasure-Threshold Curve (执行 `eval.py` 请指定指标 `fmeasure`)
    - Emeasure-Threshold Curve (执行 `eval.py` 请指定指标 `em`)
    - Precision-Recall Curve (执行 `eval.py` 请指定指标 `precision` 和 `recall`，这一点不同于以前的版本，因为 `precision` 和 `recall` 的计算被从 `fmeasure` 中独立出来了)
  + 支持评估*二值图像*, 例如常见的二值分割任务.
    - binary Fmeasure
    - binary Precision
    - binary Recall
    - binary IoU
    - binary Dice
    - binary Specificity
    - binary BER
* 更丰富的功能.
  + 支持根据配置评估模型.
  + 支持根据配置和评估结果绘制 PR 曲线和 F-measure 曲线.
  + 支持导出测试结果到 TXT 文件中.**目前由于多线程的使用, 存在提示信息额外写入的问题, 有待优化.**
  + 支持导出结果到 XLSX 文件(2021年01月04日重新提供支持).
  + 支持从生成的 `.npy` 文件导出 LaTeX 表格代码, 同时支持对最优的前三个方法用不同颜色进行标记.
  + 其他更多功能有待发觉:>.

## 使用方法

### 安装依赖

先安装相关依赖库: `pip install -r requirements.txt` .

其中指标评估是基于本人的另一个项目: [PySODMetrics](https://github.com/lartpang/PySODMetrics), 欢迎捉BUG!

### 配置数据集与方法预测的路径信息

本项目依赖于json文件存放数据, `./examples` 中已经提供了数据集和方法配置的例子: `config_dataset_json_example.json` 和 `config_method_json_example.json` , 可以至直接修改他们用于后续步骤.

[注意]
* 请注意, 由于本项目依赖于 OpenCV 读取图片, 所以请确保路径字符串不包含非 ASCII 字符.
* 请务必确保*数据集配置文件中数据集的名字*和方法配置文件中*数据集的名字*一致. 准备好json文件后, 建议使用提供的 `tools/check_path.py` 来检查下json文件中的路径信息是否正常.

<details>
<summary>
关于配置的更多细节
</summary>

例子 1: 数据集配置

注意, 这里的 "image" 是非必要的. 实际评估仅仅读取 "mask".

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

这里 `path` 表示存放图像数据的目录. 而 `prefix` 和 `suffix` 表示实际预测图像和真值图像中除去共有部分外的前缀预后缀内容.

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

* 前述步骤一切正常后, 可以开始评估了. 评估脚本用法可参考命令 `python eval.py --help` 的输出.
* 根据自己需求添加配置项并执行即可. 如无异常, 会生成指定文件名的结果文件.
* 如果不指定所有的文件, 那么就直接输出结果, 具体可见 `eval.py` 的帮助信息.
* 如指定`--curves-npy`, 绘图相关的指标信息将会保存到对应的`.npy`文件中.
* [可选] 可以使用 `tools/converter.py` 直接从生成的npy文件中导出latex表格代码.

### 为灰度图像的评估绘制曲线

可以使用 `plot.py` 来读取 `.npy` 文件按需对指定方法和数据集的结果整理并绘制 `PR` , `F-measure` 和 `E-measure` 曲线. 该脚本用法可见 `python plot.py --help` 的输出. 按照自己需求添加配置项并执行即可.

最基本的一条是请按照子图数量, 合理地指定配置文件中的 `figure.figsize` 项的数值.

### 一个基本的执行流程

这里以我自己本地的configs文件夹中的RGB SOD的配置(需要根据实际情况进行必要的修改)为例.

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
# --separated-legend 使用独立的图示
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

## 小提示

* 一些方法提供的结果名字预原始数据集真值的名字不一致
  + [注意] (2021-11-18) 当前同时提供了对名称前缀与后缀的支持, 所以基本不用用户自己改名字了.
  + [可选] 可以使用提供的脚本 `tools/rename.py` 来批量修改文件名.**请小心使用, 以避免数据被覆盖.**
  + [可选] 其他的工具: 例如 Linux 上的 `rename`, Windows 上的 [`Microsoft PowerToys`](https://github.com/microsoft/PowerToys)

## 编程参考

* Python_Openpyxl: <https://www.cnblogs.com/programmer-tlh/p/10461353.html>
* Python之re模块: <https://www.cnblogs.com/shenjianping/p/11647473.html>

## 更新日志

* 2023年3月23日
    1. 修复绘图代码中的一些问题。
    2. 完善对于 E-measure 绘图的支持。
    3. 补充一些绘图的展示，这里以我自己的 RGB-D SOD 论文 CAVER (TIP 2023) 的论文结果为例。
* 2023年3月20日
    1. 提供更丰富的指标的支持。
    2. 更新`readme.md`和示例文件。
    3. 提供更灵活的接口。
    4. 更新指标库版本。
* 2022年5月15日
    - 代码优化
* 2022年4月23日
    - 为了便于使用和配置，对大量代码进行了调整和修改，与之前版本相比，使用上也存在部分差异。
    - 评估部分：
      - 支持多个方法的json文件同时使用评估。
      - 更新了指标统计类，便于更灵活的指定不同的指标。
      - 对一些医学二值分割的指标提供了支持。
    - 绘图部分：
      - 支持多个曲线npy文件同时用于绘图。
      - 将个性化配置尽可能独立出来，提供了独立的绘图配置文件。
      - 重构了绘图类，便于使用yaml文件对matplotlib的默认设定进行覆盖。
* 2021年11月18日
    1. 改正拼写错误，调整命名。
    2. 支持预测结果中使用名称前缀 (例子可见`examples`文件夹中的`config_method_json_example.json`)，现在搭配后缀，基本上可以应对所有可能的情形了。但是需要说明的是，目前不支持使用文件提供的映射关系，请确保预测名字中包含真值（不包含扩展名）名字。
    3. 优化了绘图中的axis的设置，由于这些设置属于非常细粒度的设定，目前暂不支持使用终端选项配置，之后可能会使用特定的配置文件，例如json等来配置相关选项。
    4. 支持绘图中使用共享的纵轴，即`sharey`，这可以用来辅助绘制独立的示例图。具体使用可见`examples`中的`plot_results.py`文件。
    5. 优化了下 `include_` 与 `exclude_` 类选项的相关函数.
    6. 添加了数据集和方法配置的json的例子。并且针对`examples`中提供的配置文件统一命名为`config_`.
    7. 绘图支持对数据名和方法名使用别名。之前都是直接从各自的 `json` 配置文件中读取键来作为绘图中显示的名字，这对于名字有特殊标记（例如名字中想补充年份或者会议名字）时的使用不太方便和灵活。所以当前支持了使用额外的 `json` 配置文件来配置映射关系。例子可见 `examples` 中的 `alias_for_plotting.json` 。
    8. 由于核心文件`eval_all.py`和`plot_results.py`的配置和调用方式发生了变化，所以为了便于大家的使用和修改，我提供了两个简单调用的`sh`文件，里面提供了这怒地各个选项的基本配置案例。linux用户可以直接使用`bash <sh_name>.sh`来执行，而windows用户麻烦些，还是自己参考着其中的配置项在终端自行配置吧！有问题欢迎提问，当然，如果大家可以提供windows直接调用的`bat`文件倒也欢迎PR哦！
* 2021年08月28日
    - 扩展`tools/converter.py`，使其支持横竖两种格式的表格, 并补充对应的文档.
* 2021年08月25日
    - 添加从生成的npy自定义导出为latex表格代码的脚本(`tools/converter.py`), 并提供了配置文件示例(`examples/converter_config.py`).
* 2021年08月24日
    - 添加多进程多线程支持, 仅支持sod、cod的代码(`metrics/cal_sod_matrics.py`), cosod的代码由于使用频率较小, 没有改写, 欢迎PR.
    - 修改对应的示例程序(`examples/eval_all.py`),
    - 其他的一些小修改.
* 2021年08月17日
    - 调整readme文档的部分内容.
    - 更新check_patch工具为命令行输入参数, 不再使用文件内编码. 并在tools文件夹中的`readme.md`文件中补充文档.
    - 在draw_curves中添加对于输入的约束和检查.
    - 使用pigar生成`requirements.txt`文件.
* 2021年06月17日
    - 修正readme.md中的关于配置文件例子的表述
    - 删除代码中python3.8+的特有语法`:=`
* 2021年06月03日
    - 调整`tools`中的文件, 并修改readme.md.
    - 在`examples`中补充了数据集配置和方法配置的python文件示例.
* 2021年05月20日
    - 添加examples文件夹, 存放一些基本的示例. 实际上到目前为止, 没必要独立出来评估单独方法的文件, 使用提供的`eval_all.py`中的`include_methods`指定特定方法即可实现目的.
    - 添加了一些工具函数, 例如用于批量重命名文件的`rename.py`, 以及用于检查json文件中路径的合法性的`check_path.py`(建议每次修改完json后, 用该工具检查下).
* 2021年04月12日
    - 移除USVOS代码到独立的仓库.
    - 移动测试结果到<./results>中, 日后会继续添加更多的模型的结果.
* 2021年03月21日
    - 正式删除需要个人定制的评估文件, ~~这部分直接会放到本仓库的Readme中的[Examples](#Examples)中, 仅供参考.（已删除, 请看最新的方式）~~
    - 将格式化输出功能调整, 直接使用包`tabulate`处理, 更加方便, 输出的格式配置更丰富, 详见<https://github.com/astanin/python-tabulate>
    - 调整原来`cal_sod_matrics`的`skipped_datasets`为:
      - `get_datasets_info`的`exclude_datasets/include_datasets`;
      - `get_methods_info`的`exclude_methods/include_methods`.
* 2021年03月14日
    - 这一版本将数据集和方法的配置方法转换为基于json文件的配置.
    - 一些配套的更改与简化.
* 2021年03月12日
    - 这一版本正式将sod的评估、绘图代码与配置分离, 主要考虑如下
        - 用户的配置是需要调整的, 这部分不适宜被git严格的监视, 也便于提交后续更新的时候, 直接忽略关于配置的更改, 即后续更新时, 用户配置部分会不再更新, 若是添加新功能, 直接调整原始的函数, 其参数默认关闭新功能, 保证用户不会受到影响.
        - sod和cosod评估方式有差异, 但是绘图方式一致, 所以现将评估绘图拆分成独立部分, 置于metrics/sod文件夹下, 之后或许或调整位置, 但这种拆分策略不变.
    - 优化了cosod的评估代码, 对sod和cosod的指标recorder部分进行了简化.
    - 不再使用独立的sod_metrics代码, 由于我已经将PySODMetrics发布到了PyPI上, 所以可以直接通过pip安装.
    - 使用添加了对于print的一个彩色增强的封装, 可见`./utils/misc.py`中的`colored_print`.
    - git不再跟踪方法配置文件和数据集配置文件, 这部分现有的作为示例, 仅供使用者独立补充和参考.
    - 修复了之前绘制Fm曲线时x的问题, 之前取反了. 详见<https://github.com/lartpang/Py-SOD-VOS-EvalToolkit/issues/2>.
sues/2>.
