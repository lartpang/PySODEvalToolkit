# 基于python的显著性目标检测和视频目标分割测评工具箱

A Python-based salient object detection and video object segmentation evaluation toolbox.

> **重要提示**，最近基于Fan的matlab代码，实现了一份更加快速和准确的指标代码<https://github.com/lartpang/PySODMetrics>，已经整合到该代码中。

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

### General/Co - RGB/RGBD - SOD

可见各自文件中的配置项。

### DAVIS 2016无监督视频目标分割任务

1. `python eval_unvos_method.py --help`
2. 配置相关项后执行代码

## 最后

~~由于本工具箱是用来评估指标，所以计算过程的正确性十分重要，但是编写能力有限，可能存在一些小问题，希望大家可以及时指出。~~

评估代码来自本人的另一个项目：<https://github.com/lartpang/PySODMetrics>，欢迎捉BUG！

## Thanks

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
