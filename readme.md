# 基于python的显著性目标检测测评工具箱

A Python-based **RGB/Co-RGB/RGB-D** salient object detection evaluation toolbox.

## TODO

* [ ] 添加测试脚本
* [ ] 添加更详细的注释
* [ ] 优化xlsx导出的代码(? 导出CSV或许更好些? 既可以当做文本文件打开, 亦可使用Excel来进行整理)
* [x] 多进程和多线程的支持.
* [X] 剥离USVOS部分的代码, 让本仓库更专注一些, 相关代码已转移到另一个仓库[PyDavis16EvalToolbox](https://github.com/lartpang/PyDavis16EvalToolbox).
* [X] 提供对输出的结果基于某个指标进行排序的功能的支持(即, 使表格更加直观), 将会在接下来的版本中添加github-page来展示动态页面.
* [X] 基于Fan的matlab代码, 我实现了一份更加快速和准确的指标代码<https://github.com/lartpang/PySODMetrics>, 已经整合到该代码中.

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
    - 纯python实现, 基于numpy和各种小trick计算各项指标, 速度有保障
    - 导出特定模型的结果到xlsx文件中（2021年01月04日重新提供支持）
    - 导出测试结果到txt文件中
    - 评估所有指定的方法, 根据评估结果绘制PR曲线和F-measure曲线

## 使用方法

由于对于数据集和方法的配置因用户而异, 所以在<https://github.com/lartpang/Py-SOD-VOS-EvalToolkit/commit/d7bcc1d74065844fe0483dc3ce3fda7d06d07bc0>
之后的版本不在更新 `configs` 文件夹中的这部分内容, 直接给出一个简单的例子, 用户可以自行修改.

**python版本的配置文件的例子可以参考 `examples` 文件夹中的 `dataset_config.py` 和 `method_config.py` .**

具体使用流程:
1. 先安装指标代码库： `pip install pysodmetrics`.
    - 评估代码来自本人的另一个项目：<https://github.com/lartpang/PySODMetrics>, 欢迎捉BUG！
2. 配置不同数据集以及方法的路径信息：
    - 本项目依赖于json文件存放数据.
    - 但是本项目提供了`tools/info_py_to_json.py`来将python格式的信息（例子可见`examples`文件夹中的`dataset_config.py`和`method_config.py`）转换为json文件. 使用方法可见`tools/readme.md`.
    - 准备好json文件后, 建议使用提供的`tools/check_path.py`来检查下路径信息是否正常.
    - **请务必确保*数据集字典的名字*和方法中配置不同*数据集字典的名字*一致**.
3. 一切正常后, 可以开始评估了.
    - **具体关于评估以及使用评估得到的`.npy`文件来绘图的例子, 可以参考 `examples` 文件夹中的 `eval_all.py` 和 `plot_results.py` .**
4. 运行`eval_all.py`, 如无异常, 默认会在 <./results> 下生成结果文件, 并将用于绘图的信息保存到`.npy`文件中.
5. 后续可以使用`plot_results.py`来读取`.npy`文件绘制`PR`曲线和`Fm`曲线.

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

## Some Tips

**For some methods, their results' names are not consistent with those of original datsets.**
* You can use the script `rename.py` in folder `tools` to modify the file names of a large number of files. **Please use with care and it is recommended to read the code carefully before use to avoid data corruption.**
* **Other useful tools**
  + Linux: `rename`
  + Windows: `Microsoft PowerToys` <https://github.com/microsoft/PowerToys>

## 编程参考

* Python_Openpyxl: <https://www.cnblogs.com/programmer-tlh/p/10461353.html>
* Python之re模块: <https://www.cnblogs.com/shenjianping/p/11647473.html>

## 更新日志

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
        - sod和cosod评估方式有差异, 但是绘图方式一致, 所以现将评估绘图拆分成独立部分, 置于metrics/sod文件夹下, 之后或许或调整位置,  但这种拆分策略不变.
    - 优化了cosod的评估代码, 对sod和cosod的指标recorder部分进行了简化.
    - 不再使用独立的sod_metrics代码, 由于我已经将PySODMetrics发布到了PyPI上, 所以可以直接通过pip安装.
    - 使用添加了对于print的一个彩色增强的封装, 可见`./utils/misc.py`中的`colored_print`.
    - git不再跟踪方法配置文件和数据集配置文件, 这部分现有的作为示例, 仅供使用者独立补充和参考.
    - 修复了之前绘制Fm曲线时x的问题, 之前取反了. 详见<https://github.com/lartpang/Py-SOD-VOS-EvalToolkit/issues/2>.
