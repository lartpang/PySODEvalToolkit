# 基于python的显著性目标检测和视频目标分割测评工具箱

A Python-based salient object detection and video object segmentation evaluation toolbox.

> **重要提示**，最近基于Fan的matlab代码，实现了一份更加快速和准确的指标代码<https://github.com/lartpang/PySODMetrics>，已经整合到该代码中。

## TODO

- [ ] 添加更详细的注释
- [ ] 优化xlsx导出的代码
- [ ] 剥离USVOS部分的代码，让本仓库更专注一些

## 重要提示

- 2021年03月14日
  - 这一版本将数据集和方法的配置方法转换为基于json文件的配置。
  - 一些配套的更改与简化。
- 2021年03月12日
  - 这一版本正式将sod的评估、绘图代码与配置分离，主要考虑如下
    - 用户的配置是需要调整的，这部分不适宜被git严格的监视，也便于提交后续更新的时候，直接忽略关于配置的更改，即后续更新时，
      用户配置部分会不再更新，若是添加新功能，直接调整原始的函数，其参数默认关闭新功能，保证用户不会受到影响。
    - sod和cosod评估方式有差异，但是绘图方式一致，所以现将评估绘图拆分成独立部分，置于metrics/sod文件夹下，之后或许或调整位置，
      但这种拆分策略不变。
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
* 针对**DAVIS 2016无监督视频目标分割**任务，提供`"J(M)", "J(O)", "J(D)", "F(M)", "F(O)", "F(D)"`等指标的评估（代码借鉴自davis官方的代码，建议使用前验证下）
  - 导出对指定的模型预测结果的评估结果
  - 表格化展示不同视频上模型预测的性能

## 使用方法

### General/Co-RGB/RGBD-SOD

由于对于数据集和方法的配置因用户而异，所以在<https://github.com/lartpang/Py-SOD-VOS-EvalToolkit/commit/d7bcc1d74065844fe0483dc3ce3fda7d06d07bc0>之后的版本不在更新`configs`文件夹中的这部分内容，直接给出一个简单的例子，用户可以自行修改。
例子可以参考之前的版本，例如：<https://github.com/lartpang/Py-SOD-VOS-EvalToolkit/tree/f9c1fd5ffeef1a58067e31b9e6d28e9eb0754c46/configs>

先安装指标代码库：

```python
pip install pysodmetrics
```

可见各自文件中的配置项。

### DAVIS 2016无监督视频目标分割任务

1. `python eval_unvos_method.py --help`
2. 配置相关项后执行代码

## 最后

~~由于本工具箱是用来评估指标，所以计算过程的正确性十分重要，但是编写能力有限，可能存在一些小问题，希望大家可以及时指出。~~

评估代码来自本人的另一个项目：<https://github.com/lartpang/PySODMetrics>，欢迎捉BUG！

## 编程参考

- Python_Openpyxl: <https://www.cnblogs.com/programmer-tlh/p/10461353.html>
- Python之re模块: <https://www.cnblogs.com/shenjianping/p/11647473.html>

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
