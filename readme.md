# 基于python的显著性目标检测和视频目标分割测评工具箱

A Python-based salient object detection and video object segmentation evaluation toolbox.

> **重要提示**，最近基于Fan的matlab代码，实现了一份更加快速和准确的指标代码<https://github.com/lartpang/PySODMetrics>，已经整合到该代码中。

## TODO

- [ ] 添加更详细的注释
- [ ] 优化xlsx导出的代码
- [ ] 剥离USVOS部分的代码，让本仓库更专注一些
- [ ] 提供对输出的结果基于某个指标进行排序的功能的支持（即，使表格更加直观）

## 重要提示

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
* 针对**DAVIS 2016无监督视频目标分割**任务，提供`"J(M)", "J(O)", "J(D)", "F(M)", "F(O)", "F(D)"`等指标的评估（代码借鉴自davis官方的代码，建议使用前验证下）
    - 导出对指定的模型预测结果的评估结果
    - 表格化展示不同视频上模型预测的性能

## 使用方法

### General/Co-RGB/RGBD-SOD

由于对于数据集和方法的配置因用户而异，所以在<https://github.com/lartpang/Py-SOD-VOS-EvalToolkit/commit/d7bcc1d74065844fe0483dc3ce3fda7d06d07bc0>
之后的版本不在更新`configs`文件夹中的这部分内容，直接给出一个简单的例子，用户可以自行修改。
例子可以参考之前的版本，例如：<https://github.com/lartpang/Py-SOD-VOS-EvalToolkit/tree/f9c1fd5ffeef1a58067e31b9e6d28e9eb0754c46/configs>

先安装指标代码库：

```python
pip
install
pysodmetrics
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

## RGBD SOD评估结果

### Dataset: LFSD

| methods    |   MAE |    SM |   adpE |   adpF |   avgE |   avgF |   maxE |   maxF |   wFm |
|------------|-------|-------|--------|--------|--------|--------|--------|--------|-------|
| HDFNet_VGG | 0.085 | 0.847 |  0.883 |  0.831 |  0.87  |  0.819 |  0.881 |  0.838 | 0.792 |
| HDFNet_VGG | 0.083 | 0.844 |  0.886 |  0.833 |  0.87  |  0.82  |  0.879 |  0.836 | 0.793 |
| HDFNet_Res | 0.076 | 0.854 |  0.891 |  0.843 |  0.883 |  0.835 |  0.896 |  0.862 | 0.806 |
| JLDCF      | 0.07  | 0.861 |  0.902 |  0.854 |  0.894 |  0.848 |  0.902 |  0.867 | 0.822 |
| CoNet      | 0.071 | 0.862 |  0.901 |  0.848 |  0.895 |  0.844 |  0.907 |  0.859 | 0.814 |
| BBSNet     | 0.072 | 0.864 |  0.901 |  0.858 |  0.883 |  0.843 |  0.901 |  0.858 | 0.814 |
| CMWNet     | 0.066 | 0.876 |  0.908 |  0.87  |  0.9   |  0.862 |  0.912 |  0.883 | 0.834 |
| FRDT       | 0.074 | 0.857 |  0.899 |  0.854 |  0.888 |  0.847 |  0.903 |  0.859 | 0.814 |
| S2MA       | 0.094 | 0.837 |  0.876 |  0.82  |  0.855 |  0.806 |  0.873 |  0.835 | 0.772 |
| UCNet      | 0.066 | 0.864 |  0.906 |  0.859 |  0.901 |  0.855 |  0.905 |  0.864 | 0.832 |
| CasGNN     | 0.073 | 0.846 |  0.877 |  0.831 |  0.88  |  0.839 |  0.888 |  0.847 | 0.81  |
| DANet_VGG1 | 0.082 | 0.845 |  0.878 |  0.826 |  0.872 |  0.826 |  0.886 |  0.846 | 0.789 |
| DANet_VGG1 | 0.079 | 0.849 |  0.881 |  0.831 |  0.871 |  0.827 |  0.881 |  0.844 | 0.795 |
| PGAR       | 0.074 | 0.853 |  0.894 |  0.852 |  0.872 |  0.831 |  0.89  |  0.844 | 0.8   |
| DisenFuse  | 0.119 | 0.789 |  0.84  |  0.768 |  0.823 |  0.75  |  0.842 |  0.771 | 0.705 |
| DPANet     | 0.072 | 0.864 |  0.899 |  0.859 |  0.882 |  0.842 |  0.891 |  0.86  | 0.814 |
| ICNet      | 0.071 | 0.868 |  0.9   |  0.861 |  0.892 |  0.852 |  0.903 |  0.871 | 0.822 |
| D3Net      | 0.095 | 0.825 |  0.863 |  0.805 |  0.848 |  0.796 |  0.862 |  0.81  | 0.76  |
| RD3D       | 0.073 | 0.858 |  0.898 |  0.855 |  0.884 |  0.843 |  0.891 |  0.854 | 0.816 |
| AFNet      | 0.133 | 0.738 |  0.81  |  0.742 |  0.796 |  0.736 |  0.815 |  0.744 | 0.671 |
| CDCP       | 0.199 | 0.659 |  0.738 |  0.635 |  0.698 |  0.605 |  0.731 |  0.63  | 0.516 |
| CPFP       | 0.088 | 0.828 |  0.867 |  0.813 |  0.863 |  0.811 |  0.872 |  0.826 | 0.775 |
| CTMF       | 0.12  | 0.796 |  0.851 |  0.781 |  0.808 |  0.754 |  0.864 |  0.792 | 0.696 |
| DCMC       | 0.155 | 0.755 |  0.842 |  0.817 |  0.678 |  0.651 |  0.858 |  0.82  | 0.598 |
| DES        | 0.415 | 0.441 |  0.49  |  0.224 |  0.446 |  0.306 |  0.574 |  0.358 | 0.273 |
| DF         | 0.142 | 0.788 |  0.841 |  0.811 |  0.713 |  0.668 |  0.874 |  0.822 | 0.641 |
| DMRA       | 0.076 | 0.847 |  0.899 |  0.849 |  0.893 |  0.845 |  0.9   |  0.856 | 0.811 |
| MB         | 0.218 | 0.539 |  0.634 |  0.545 |  0.579 |  0.476 |  0.706 |  0.592 | 0.392 |
| MMCI       | 0.132 | 0.787 |  0.84  |  0.779 |  0.775 |  0.722 |  0.838 |  0.771 | 0.663 |
| NLPR       | 0.21  | 0.56  |  0.743 |  0.709 |  0.492 |  0.394 |  0.784 |  0.712 | 0.375 |
| PCANet     | 0.112 | 0.8   |  0.856 |  0.794 |  0.82  |  0.763 |  0.842 |  0.786 | 0.716 |
| PDNet      | 0.109 | 0.845 |  0.872 |  0.824 |  0.821 |  0.777 |  0.875 |  0.836 | 0.734 |
| TANet      | 0.111 | 0.801 |  0.851 |  0.794 |  0.821 |  0.771 |  0.847 |  0.796 | 0.719 |

### Dataset: NJUD

| methods    |   MAE |    SM |   adpE |   adpF |   avgE |   avgF |   maxE |   maxF |   wFm |
|------------|-------|-------|--------|--------|--------|--------|--------|--------|-------|
| HDFNet_VGG | 0.037 | 0.911 |  0.934 |  0.894 |  0.938 |  0.898 |  0.945 |  0.913 | 0.881 |
| HDFNet_VGG | 0.038 | 0.911 |  0.932 |  0.887 |  0.937 |  0.893 |  0.947 |  0.913 | 0.877 |
| HDFNet_Res | 0.038 | 0.908 |  0.932 |  0.889 |  0.936 |  0.892 |  0.944 |  0.911 | 0.877 |
| JLDCF      | 0.041 | 0.902 |  0.935 |  0.885 |  0.935 |  0.885 |  0.944 |  0.904 | 0.869 |
| CoNet      | 0.046 | 0.896 |  0.924 |  0.872 |  0.924 |  0.874 |  0.937 |  0.893 | 0.848 |
| BBSNet     | 0.035 | 0.921 |  0.942 |  0.902 |  0.938 |  0.902 |  0.949 |  0.92  | 0.884 |
| CMWNet     | 0.046 | 0.903 |  0.923 |  0.88  |  0.923 |  0.881 |  0.936 |  0.902 | 0.857 |
| FRDT       | 0.048 | 0.898 |  0.919 |  0.877 |  0.921 |  0.882 |  0.933 |  0.899 | 0.855 |
| S2MA       | 0.053 | 0.894 |  0.916 |  0.865 |  0.914 |  0.865 |  0.93  |  0.889 | 0.842 |
| UCNet      | 0.043 | 0.897 |  0.934 |  0.889 |  0.93  |  0.885 |  0.936 |  0.895 | 0.868 |
| DANet_VGG1 | 0.046 | 0.897 |  0.926 |  0.877 |  0.921 |  0.874 |  0.936 |  0.893 | 0.853 |
| DANet_VGG1 | 0.045 | 0.899 |  0.922 |  0.871 |  0.922 |  0.879 |  0.935 |  0.898 | 0.857 |
| PGAR       | 0.042 | 0.909 |  0.935 |  0.893 |  0.929 |  0.892 |  0.94  |  0.907 | 0.872 |
| DisenFuse  | 0.052 | 0.889 |  0.914 |  0.859 |  0.913 |  0.86  |  0.928 |  0.886 | 0.831 |
| DPANet     | 0.035 | 0.92  |  0.933 |  0.886 |  0.937 |  0.898 |  0.949 |  0.918 | 0.882 |
| ICNet      | 0.052 | 0.894 |  0.913 |  0.868 |  0.914 |  0.869 |  0.926 |  0.891 | 0.843 |
| D3Net      | 0.046 | 0.9   |  0.916 |  0.865 |  0.922 |  0.879 |  0.939 |  0.9   | 0.854 |
| RD3D       | 0.036 | 0.916 |  0.942 |  0.901 |  0.94  |  0.901 |  0.947 |  0.914 | 0.886 |
| AFNet      | 0.1   | 0.772 |  0.847 |  0.768 |  0.826 |  0.764 |  0.853 |  0.775 | 0.696 |
| CDCP       | 0.182 | 0.674 |  0.751 |  0.618 |  0.717 |  0.597 |  0.747 |  0.619 | 0.508 |
| CPFP       | 0.053 | 0.878 |  0.9   |  0.837 |  0.91  |  0.85  |  0.923 |  0.877 | 0.828 |
| CTMF       | 0.085 | 0.849 |  0.866 |  0.788 |  0.847 |  0.779 |  0.913 |  0.845 | 0.72  |
| DCMC       | 0.167 | 0.704 |  0.797 |  0.716 |  0.63  |  0.57  |  0.806 |  0.729 | 0.494 |
| DES        | 0.448 | 0.413 |  0.484 |  0.16  |  0.414 |  0.268 |  0.56  |  0.306 | 0.233 |
| DF         | 0.151 | 0.737 |  0.818 |  0.744 |  0.669 |  0.605 |  0.833 |  0.757 | 0.544 |
| DMRA       | 0.051 | 0.886 |  0.92  |  0.871 |  0.919 |  0.872 |  0.927 |  0.886 | 0.846 |
| MB         | 0.203 | 0.536 |  0.647 |  0.494 |  0.591 |  0.439 |  0.706 |  0.548 | 0.353 |
| MMCI       | 0.079 | 0.859 |  0.882 |  0.813 |  0.851 |  0.794 |  0.915 |  0.853 | 0.739 |
| NLPR       | 0.201 | 0.532 |  0.724 |  0.626 |  0.465 |  0.342 |  0.719 |  0.61  | 0.303 |
| PCANet     | 0.059 | 0.877 |  0.909 |  0.844 |  0.895 |  0.84  |  0.924 |  0.872 | 0.803 |
| TANet      | 0.061 | 0.878 |  0.909 |  0.844 |  0.895 |  0.841 |  0.925 |  0.874 | 0.803 |

### Dataset: NLPR

| methods    |   MAE |    SM |   adpE |   adpF |   avgE |   avgF |   maxE |   maxF |   wFm |
|------------|-------|-------|--------|--------|--------|--------|--------|--------|-------|
| HDFNet_VGG | 0.027 | 0.916 |  0.948 |  0.878 |  0.946 |  0.884 |  0.956 |  0.904 | 0.869 |
| HDFNet_VGG | 0.027 | 0.915 |  0.951 |  0.883 |  0.947 |  0.885 |  0.955 |  0.904 | 0.871 |
| HDFNet_Res | 0.023 | 0.923 |  0.957 |  0.889 |  0.955 |  0.894 |  0.963 |  0.917 | 0.882 |
| JLDCF      | 0.022 | 0.925 |  0.955 |  0.878 |  0.955 |  0.894 |  0.963 |  0.918 | 0.882 |
| CoNet      | 0.031 | 0.908 |  0.933 |  0.845 |  0.933 |  0.864 |  0.945 |  0.887 | 0.841 |
| BBSNet     | 0.023 | 0.93  |  0.953 |  0.882 |  0.95  |  0.896 |  0.961 |  0.918 | 0.879 |
| CMWNet     | 0.029 | 0.917 |  0.94  |  0.859 |  0.939 |  0.877 |  0.951 |  0.903 | 0.856 |
| FRDT       | 0.029 | 0.914 |  0.946 |  0.87  |  0.939 |  0.881 |  0.95  |  0.9   | 0.857 |
| S2MA       | 0.03  | 0.915 |  0.942 |  0.853 |  0.937 |  0.873 |  0.953 |  0.902 | 0.852 |
| UCNet      | 0.025 | 0.92  |  0.955 |  0.89  |  0.951 |  0.891 |  0.956 |  0.903 | 0.878 |
| CasGNN     | 0.025 | 0.919 |  0.952 |  0.891 |  0.948 |  0.894 |  0.955 |  0.906 | 0.88  |
| DANet_VGG1 | 0.031 | 0.909 |  0.945 |  0.865 |  0.933 |  0.871 |  0.949 |  0.894 | 0.85  |
| DANet_VGG1 | 0.028 | 0.915 |  0.949 |  0.87  |  0.94  |  0.88  |  0.953 |  0.903 | 0.862 |
| PGAR       | 0.024 | 0.93  |  0.955 |  0.885 |  0.949 |  0.896 |  0.961 |  0.916 | 0.881 |
| DisenFuse  | 0.035 | 0.9   |  0.933 |  0.839 |  0.928 |  0.855 |  0.944 |  0.881 | 0.828 |
| DPANet     | 0.024 | 0.928 |  0.955 |  0.875 |  0.949 |  0.89  |  0.962 |  0.913 | 0.875 |
| ICNet      | 0.028 | 0.923 |  0.945 |  0.87  |  0.941 |  0.884 |  0.952 |  0.908 | 0.864 |
| D3Net      | 0.03  | 0.912 |  0.945 |  0.861 |  0.936 |  0.872 |  0.953 |  0.897 | 0.849 |
| RD3D       | 0.022 | 0.93  |  0.959 |  0.892 |  0.957 |  0.903 |  0.965 |  0.919 | 0.889 |
| AFNet      | 0.058 | 0.799 |  0.884 |  0.747 |  0.851 |  0.755 |  0.879 |  0.771 | 0.693 |
| CDCP       | 0.115 | 0.726 |  0.785 |  0.59  |  0.772 |  0.6   |  0.817 |  0.647 | 0.5   |
| CPFP       | 0.038 | 0.884 |  0.92  |  0.818 |  0.914 |  0.835 |  0.929 |  0.862 | 0.807 |
| CTMF       | 0.056 | 0.86  |  0.869 |  0.724 |  0.84  |  0.74  |  0.929 |  0.825 | 0.679 |
| DCMC       | 0.196 | 0.551 |  0.684 |  0.328 |  0.585 |  0.304 |  0.694 |  0.375 | 0.257 |
| DES        | 0.301 | 0.582 |  0.758 |  0.581 |  0.552 |  0.436 |  0.813 |  0.649 | 0.253 |
| DF         | 0.1   | 0.771 |  0.837 |  0.681 |  0.716 |  0.599 |  0.833 |  0.706 | 0.514 |
| DMRA       | 0.031 | 0.899 |  0.941 |  0.853 |  0.939 |  0.864 |  0.947 |  0.879 | 0.838 |
| MB         | 0.09  | 0.716 |  0.816 |  0.636 |  0.793 |  0.622 |  0.806 |  0.631 | 0.557 |
| MMCI       | 0.059 | 0.856 |  0.872 |  0.73  |  0.841 |  0.737 |  0.913 |  0.815 | 0.676 |
| NLPR       | 0.119 | 0.592 |  0.774 |  0.519 |  0.534 |  0.354 |  0.714 |  0.493 | 0.311 |
| PCANet     | 0.044 | 0.874 |  0.916 |  0.795 |  0.887 |  0.803 |  0.925 |  0.841 | 0.762 |
| TANet      | 0.041 | 0.886 |  0.916 |  0.795 |  0.901 |  0.819 |  0.941 |  0.863 | 0.779 |

### Dataset: RGBD135

| methods    |   MAE |    SM |   adpE |   adpF |   avgE |   avgF |   maxE |   maxF |   wFm |
|------------|-------|-------|--------|--------|--------|--------|--------|--------|-------|
| HDFNet_VGG | 0.02  | 0.932 |  0.973 |  0.919 |  0.959 |  0.914 |  0.971 |  0.924 | 0.902 |
| HDFNet_VGG | 0.017 | 0.937 |  0.976 |  0.918 |  0.969 |  0.92  |  0.977 |  0.935 | 0.913 |
| HDFNet_Res | 0.021 | 0.926 |  0.971 |  0.912 |  0.957 |  0.91  |  0.97  |  0.921 | 0.895 |
| JLDCF      | 0.02  | 0.931 |  0.969 |  0.9   |  0.959 |  0.907 |  0.968 |  0.923 | 0.894 |
| CoNet      | 0.028 | 0.91  |  0.945 |  0.87  |  0.93  |  0.877 |  0.945 |  0.896 | 0.848 |
| BBSNet     | 0.021 | 0.933 |  0.967 |  0.906 |  0.949 |  0.91  |  0.966 |  0.927 | 0.89  |
| CMWNet     | 0.022 | 0.934 |  0.967 |  0.9   |  0.955 |  0.909 |  0.969 |  0.93  | 0.888 |
| FRDT       | 0.03  | 0.9   |  0.94  |  0.874 |  0.917 |  0.873 |  0.938 |  0.886 | 0.838 |
| S2MA       | 0.021 | 0.941 |  0.974 |  0.906 |  0.952 |  0.908 |  0.973 |  0.935 | 0.892 |
| UCNet      | 0.018 | 0.933 |  0.974 |  0.917 |  0.967 |  0.919 |  0.976 |  0.93  | 0.908 |
| CasGNN     | 0.028 | 0.894 |  0.937 |  0.891 |  0.92  |  0.884 |  0.937 |  0.894 | 0.851 |
| DANet_VGG1 | 0.028 | 0.905 |  0.961 |  0.891 |  0.922 |  0.877 |  0.958 |  0.895 | 0.848 |
| DANet_VGG1 | 0.023 | 0.924 |  0.968 |  0.899 |  0.942 |  0.896 |  0.966 |  0.914 | 0.877 |
| PGAR       | 0.026 | 0.913 |  0.939 |  0.88  |  0.924 |  0.886 |  0.945 |  0.902 | 0.855 |
| DisenFuse  | 0.04  | 0.877 |  0.923 |  0.82  |  0.896 |  0.823 |  0.921 |  0.845 | 0.779 |
| DPANet     | 0.023 | 0.919 |  0.963 |  0.9   |  0.929 |  0.891 |  0.958 |  0.912 | 0.868 |
| ICNet      | 0.027 | 0.92  |  0.959 |  0.889 |  0.941 |  0.893 |  0.96  |  0.913 | 0.867 |
| D3Net      | 0.031 | 0.898 |  0.951 |  0.87  |  0.911 |  0.86  |  0.945 |  0.885 | 0.829 |
| RD3D       | 0.019 | 0.935 |  0.975 |  0.917 |  0.961 |  0.917 |  0.972 |  0.929 | 0.904 |
| AFNet      | 0.068 | 0.77  |  0.874 |  0.73  |  0.809 |  0.713 |  0.881 |  0.729 | 0.641 |
| CDCP       | 0.12  | 0.711 |  0.81  |  0.594 |  0.763 |  0.575 |  0.82  |  0.618 | 0.476 |
| CPFP       | 0.038 | 0.872 |  0.927 |  0.829 |  0.888 |  0.824 |  0.923 |  0.846 | 0.787 |
| CTMF       | 0.055 | 0.863 |  0.911 |  0.778 |  0.826 |  0.756 |  0.932 |  0.844 | 0.686 |
| DCMC       | 0.196 | 0.47  |  0.677 |  0.235 |  0.512 |  0.194 |  0.63  |  0.275 | 0.167 |
| DES        | 0.289 | 0.632 |  0.814 |  0.693 |  0.579 |  0.495 |  0.858 |  0.764 | 0.301 |
| DF         | 0.131 | 0.687 |  0.806 |  0.574 |  0.653 |  0.472 |  0.822 |  0.594 | 0.391 |
| DMRA       | 0.03  | 0.9   |  0.944 |  0.865 |  0.932 |  0.872 |  0.942 |  0.888 | 0.842 |
| MB         | 0.104 | 0.663 |  0.798 |  0.597 |  0.769 |  0.575 |  0.788 |  0.6   | 0.501 |
| MMCI       | 0.065 | 0.848 |  0.904 |  0.762 |  0.825 |  0.735 |  0.928 |  0.822 | 0.65  |
| NLPR       | 0.1   | 0.573 |  0.844 |  0.847 |  0.472 |  0.401 |  0.933 |  0.92  | 0.357 |
| PCANet     | 0.05  | 0.843 |  0.911 |  0.774 |  0.836 |  0.761 |  0.891 |  0.802 | 0.71  |
| TANet      | 0.046 | 0.858 |  0.919 |  0.795 |  0.863 |  0.79  |  0.91  |  0.828 | 0.738 |

### Dataset: SIP

| methods    |   MAE |    SM |   adpE |   adpF |   avgE |   avgF |   maxE |   maxF |   wFm |
|------------|-------|-------|--------|--------|--------|--------|--------|--------|-------|
| HDFNet_VGG | 0.05  | 0.878 |  0.92  |  0.863 |  0.916 |  0.863 |  0.922 |  0.886 | 0.835 |
| HDFNet_VGG | 0.047 | 0.885 |  0.924 |  0.87  |  0.92  |  0.87  |  0.927 |  0.891 | 0.844 |
| HDFNet_Res | 0.047 | 0.886 |  0.924 |  0.875 |  0.922 |  0.875 |  0.93  |  0.894 | 0.848 |
| JLDCF      | 0.049 | 0.88  |  0.923 |  0.873 |  0.918 |  0.873 |  0.925 |  0.889 | 0.844 |
| CoNet      | 0.063 | 0.858 |  0.909 |  0.841 |  0.901 |  0.844 |  0.913 |  0.867 | 0.802 |
| BBSNet     | 0.055 | 0.879 |  0.917 |  0.872 |  0.906 |  0.868 |  0.922 |  0.883 | 0.83  |
| CMWNet     | 0.062 | 0.867 |  0.909 |  0.851 |  0.9   |  0.851 |  0.913 |  0.874 | 0.811 |
| S2MA       | 0.057 | 0.872 |  0.913 |  0.854 |  0.905 |  0.854 |  0.919 |  0.877 | 0.819 |
| UCNet      | 0.051 | 0.875 |  0.918 |  0.868 |  0.914 |  0.867 |  0.919 |  0.879 | 0.836 |
| DANet_VGG1 | 0.054 | 0.878 |  0.917 |  0.864 |  0.91  |  0.864 |  0.921 |  0.884 | 0.829 |
| DANet_VGG1 | 0.054 | 0.875 |  0.915 |  0.855 |  0.908 |  0.854 |  0.918 |  0.876 | 0.822 |
| PGAR       | 0.055 | 0.876 |  0.912 |  0.854 |  0.906 |  0.854 |  0.915 |  0.876 | 0.822 |
| DisenFuse  | 0.068 | 0.859 |  0.899 |  0.819 |  0.893 |  0.82  |  0.911 |  0.852 | 0.78  |
| DPANet     | 0.051 | 0.883 |  0.922 |  0.865 |  0.914 |  0.865 |  0.925 |  0.886 | 0.833 |
| ICNet      | 0.069 | 0.854 |  0.9   |  0.836 |  0.89  |  0.835 |  0.903 |  0.857 | 0.791 |
| D3Net      | 0.063 | 0.86  |  0.902 |  0.835 |  0.897 |  0.838 |  0.909 |  0.861 | 0.799 |
| RD3D       | 0.048 | 0.885 |  0.924 |  0.874 |  0.918 |  0.873 |  0.924 |  0.889 | 0.845 |
| AFNet      | 0.118 | 0.72  |  0.815 |  0.705 |  0.793 |  0.702 |  0.819 |  0.712 | 0.617 |
| CDCP       | 0.224 | 0.595 |  0.722 |  0.495 |  0.683 |  0.482 |  0.721 |  0.505 | 0.397 |
| CPFP       | 0.064 | 0.85  |  0.899 |  0.819 |  0.893 |  0.821 |  0.903 |  0.851 | 0.788 |
| CTMF       | 0.139 | 0.716 |  0.824 |  0.684 |  0.704 |  0.608 |  0.829 |  0.694 | 0.535 |
| DCMC       | 0.186 | 0.683 |  0.786 |  0.645 |  0.598 |  0.5   |  0.743 |  0.618 | 0.413 |
| DES        | 0.298 | 0.616 |  0.751 |  0.644 |  0.564 |  0.496 |  0.77  |  0.669 | 0.342 |
| DF         | 0.185 | 0.653 |  0.794 |  0.673 |  0.565 |  0.465 |  0.759 |  0.657 | 0.406 |
| DMRA       | 0.086 | 0.806 |  0.863 |  0.818 |  0.843 |  0.81  |  0.874 |  0.821 | 0.739 |
| MMCI       | 0.086 | 0.833 |  0.886 |  0.795 |  0.845 |  0.771 |  0.897 |  0.818 | 0.712 |
| NLPR       | 0.184 | 0.511 |  0.719 |  0.592 |  0.436 |  0.287 |  0.716 |  0.574 | 0.256 |
| PCANet     | 0.071 | 0.842 |  0.9   |  0.825 |  0.878 |  0.814 |  0.901 |  0.838 | 0.768 |
| TANet      | 0.075 | 0.835 |  0.894 |  0.809 |  0.87  |  0.803 |  0.895 |  0.83  | 0.748 |

### Dataset: SSD

| methods    |   MAE |    SM |   adpE |   adpF |   avgE |   avgF |   maxE |   maxF |   wFm |
|------------|-------|-------|--------|--------|--------|--------|--------|--------|-------|
| HDFNet_VGG | 0.048 | 0.866 |  0.913 |  0.844 |  0.899 |  0.833 |  0.909 |  0.849 | 0.808 |
| HDFNet_VGG | 0.046 | 0.875 |  0.911 |  0.847 |  0.905 |  0.848 |  0.913 |  0.861 | 0.819 |
| HDFNet_Res | 0.045 | 0.879 |  0.911 |  0.842 |  0.912 |  0.849 |  0.925 |  0.87  | 0.821 |
| CoNet      | 0.06  | 0.853 |  0.898 |  0.805 |  0.898 |  0.818 |  0.915 |  0.84  | 0.779 |
| BBSNet     | 0.044 | 0.882 |  0.92  |  0.849 |  0.904 |  0.843 |  0.919 |  0.859 | 0.811 |
| CMWNet     | 0.051 | 0.875 |  0.902 |  0.82  |  0.906 |  0.837 |  0.93  |  0.871 | 0.795 |
| FRDT       | 0.054 | 0.872 |  0.904 |  0.824 |  0.907 |  0.842 |  0.924 |  0.865 | 0.801 |
| S2MA       | 0.052 | 0.868 |  0.898 |  0.818 |  0.89  |  0.823 |  0.909 |  0.848 | 0.787 |
| CasGNN     | 0.047 | 0.872 |  0.915 |  0.841 |  0.915 |  0.85  |  0.923 |  0.863 | 0.826 |
| DANet_VGG1 | 0.05  | 0.869 |  0.909 |  0.831 |  0.894 |  0.833 |  0.907 |  0.852 | 0.798 |
| DANet_VGG1 | 0.05  | 0.864 |  0.911 |  0.827 |  0.892 |  0.826 |  0.914 |  0.843 | 0.795 |
| DPANet     | 0.042 | 0.889 |  0.924 |  0.849 |  0.914 |  0.856 |  0.927 |  0.881 | 0.826 |
| ICNet      | 0.064 | 0.848 |  0.879 |  0.799 |  0.887 |  0.815 |  0.902 |  0.841 | 0.772 |
| D3Net      | 0.058 | 0.857 |  0.904 |  0.814 |  0.891 |  0.815 |  0.91  |  0.834 | 0.777 |
| AFNet      | 0.118 | 0.714 |  0.803 |  0.694 |  0.762 |  0.672 |  0.807 |  0.687 | 0.589 |
| CDCP       | 0.219 | 0.605 |  0.713 |  0.523 |  0.69  |  0.524 |  0.72  |  0.543 | 0.426 |
| CPFP       | 0.082 | 0.807 |  0.832 |  0.726 |  0.839 |  0.747 |  0.852 |  0.766 | 0.708 |
| CTMF       | 0.1   | 0.776 |  0.838 |  0.709 |  0.793 |  0.687 |  0.864 |  0.729 | 0.621 |
| DCMC       | 0.168 | 0.707 |  0.789 |  0.683 |  0.642 |  0.569 |  0.792 |  0.713 | 0.478 |
| DES        | 0.5   | 0.341 |  0.466 |  0.07  |  0.374 |  0.193 |  0.564 |  0.253 | 0.171 |
| DF         | 0.151 | 0.743 |  0.801 |  0.708 |  0.68  |  0.613 |  0.814 |  0.731 | 0.533 |
| DMRA       | 0.059 | 0.857 |  0.898 |  0.82  |  0.897 |  0.827 |  0.906 |  0.844 | 0.784 |
| MB         | 0.219 | 0.499 |  0.637 |  0.416 |  0.556 |  0.357 |  0.666 |  0.457 | 0.276 |
| MMCI       | 0.082 | 0.814 |  0.86  |  0.748 |  0.796 |  0.722 |  0.883 |  0.782 | 0.661 |
| NLPR       | 0.2   | 0.563 |  0.726 |  0.55  |  0.508 |  0.366 |  0.709 |  0.535 | 0.313 |
| PCANet     | 0.063 | 0.843 |  0.889 |  0.785 |  0.854 |  0.774 |  0.899 |  0.811 | 0.731 |
| TANet      | 0.063 | 0.839 |  0.886 |  0.766 |  0.86  |  0.773 |  0.897 |  0.81  | 0.726 |

### Dataset: STEREO1000

| methods    |   MAE |    SM |   adpE |   adpF |   avgE |   avgF |   maxE |   maxF |   wFm |
|------------|-------|-------|--------|--------|--------|--------|--------|--------|-------|
| HDFNet_VGG | 0.039 | 0.906 |  0.937 |  0.879 |  0.936 |  0.881 |  0.947 |  0.908 | 0.863 |
| HDFNet_VGG | 0.04  | 0.903 |  0.934 |  0.875 |  0.932 |  0.878 |  0.941 |  0.901 | 0.859 |
| HDFNet_Res | 0.041 | 0.9   |  0.931 |  0.867 |  0.931 |  0.87  |  0.943 |  0.9   | 0.853 |
| JLDCF      | 0.04  | 0.903 |  0.937 |  0.869 |  0.935 |  0.873 |  0.947 |  0.904 | 0.857 |
| CoNet      | 0.038 | 0.905 |  0.941 |  0.883 |  0.94  |  0.886 |  0.947 |  0.901 | 0.865 |
| BBSNet     | 0.041 | 0.908 |  0.941 |  0.885 |  0.928 |  0.883 |  0.942 |  0.903 | 0.858 |
| CMWNet     | 0.043 | 0.905 |  0.93  |  0.869 |  0.928 |  0.872 |  0.944 |  0.901 | 0.847 |
| S2MA       | 0.051 | 0.89  |  0.926 |  0.855 |  0.914 |  0.853 |  0.932 |  0.882 | 0.825 |
| UCNet      | 0.039 | 0.903 |  0.942 |  0.885 |  0.938 |  0.884 |  0.944 |  0.899 | 0.867 |
| CasGNN     | 0.039 | 0.899 |  0.929 |  0.876 |  0.934 |  0.89  |  0.943 |  0.901 | 0.867 |
| DANet_VGG1 | 0.047 | 0.892 |  0.926 |  0.858 |  0.915 |  0.857 |  0.93  |  0.882 | 0.83  |
| DANet_VGG1 | 0.043 | 0.901 |  0.931 |  0.868 |  0.923 |  0.87  |  0.937 |  0.892 | 0.846 |
| PGAR       | 0.041 | 0.907 |  0.937 |  0.88  |  0.927 |  0.878 |  0.939 |  0.898 | 0.856 |
| DisenFuse  | 0.054 | 0.883 |  0.915 |  0.841 |  0.909 |  0.843 |  0.926 |  0.872 | 0.811 |
| ICNet      | 0.045 | 0.903 |  0.926 |  0.865 |  0.926 |  0.87  |  0.942 |  0.898 | 0.844 |
| D3Net      | 0.046 | 0.899 |  0.924 |  0.859 |  0.92  |  0.866 |  0.938 |  0.891 | 0.838 |
| RD3D       | 0.037 | 0.911 |  0.944 |  0.886 |  0.939 |  0.888 |  0.947 |  0.906 | 0.871 |
| AFNet      | 0.075 | 0.825 |  0.887 |  0.807 |  0.872 |  0.806 |  0.887 |  0.823 | 0.752 |
| CDCP       | 0.149 | 0.713 |  0.796 |  0.666 |  0.751 |  0.638 |  0.786 |  0.664 | 0.558 |
| CPFP       | 0.051 | 0.879 |  0.907 |  0.83  |  0.911 |  0.841 |  0.925 |  0.874 | 0.817 |
| CTMF       | 0.086 | 0.848 |  0.87  |  0.771 |  0.841 |  0.758 |  0.912 |  0.831 | 0.698 |
| DCMC       | 0.148 | 0.731 |  0.831 |  0.742 |  0.655 |  0.59  |  0.819 |  0.74  | 0.52  |
| DES        | 0.295 | 0.642 |  0.696 |  0.594 |  0.58  |  0.519 |  0.811 |  0.7   | 0.375 |
| DF         | 0.141 | 0.757 |  0.838 |  0.742 |  0.692 |  0.617 |  0.847 |  0.757 | 0.549 |
| DMRA       | 0.087 | 0.752 |  0.816 |  0.762 |  0.764 |  0.71  |  0.827 |  0.743 | 0.647 |
| MMCI       | 0.068 | 0.873 |  0.905 |  0.829 |  0.873 |  0.813 |  0.927 |  0.863 | 0.76  |
| NLPR       | 0.172 | 0.562 |  0.77  |  0.703 |  0.484 |  0.378 |  0.771 |  0.683 | 0.346 |
| PCANet     | 0.064 | 0.875 |  0.907 |  0.826 |  0.887 |  0.818 |  0.925 |  0.86  | 0.778 |
| TANet      | 0.06  | 0.871 |  0.916 |  0.835 |  0.893 |  0.828 |  0.923 |  0.861 | 0.787 |

### Dataset: DUTRGBD

| methods    |   MAE |    SM |   adpE |   adpF |   avgE |   avgF |   maxE |   maxF |   wFm |
|------------|-------|-------|--------|--------|--------|--------|--------|--------|-------|
| HDFNet_VGG | 0.04  | 0.905 |  0.938 |  0.892 |  0.929 |  0.889 |  0.94  |  0.908 | 0.865 |
| HDFNet_VGG | 0.039 | 0.911 |  0.941 |  0.894 |  0.937 |  0.894 |  0.949 |  0.923 | 0.871 |
| HDFNet_Res | 0.041 | 0.907 |  0.938 |  0.885 |  0.934 |  0.886 |  0.947 |  0.918 | 0.864 |
| JLDCF      | 0.043 | 0.905 |  0.938 |  0.883 |  0.932 |  0.884 |  0.943 |  0.911 | 0.863 |
| CoNet      | 0.034 | 0.919 |  0.952 |  0.908 |  0.947 |  0.91  |  0.956 |  0.927 | 0.89  |
| BBSNet     | 0.038 | 0.912 |  0.945 |  0.904 |  0.932 |  0.9   |  0.945 |  0.918 | 0.874 |
| CMWNet     | 0.056 | 0.887 |  0.922 |  0.866 |  0.912 |  0.864 |  0.926 |  0.888 | 0.831 |
| FRDT       | 0.039 | 0.91  |  0.941 |  0.902 |  0.938 |  0.904 |  0.948 |  0.919 | 0.877 |
| S2MA       | 0.044 | 0.903 |  0.935 |  0.885 |  0.928 |  0.883 |  0.937 |  0.9   | 0.862 |
| UCNet      | 0.057 | 0.864 |  0.906 |  0.855 |  0.899 |  0.851 |  0.904 |  0.857 | 0.82  |
| CasGNN     | 0.03  | 0.921 |  0.949 |  0.917 |  0.947 |  0.919 |  0.954 |  0.928 | 0.902 |
| DANet_VGG1 | 0.047 | 0.889 |  0.929 |  0.884 |  0.917 |  0.88  |  0.931 |  0.895 | 0.847 |
| DANet_VGG1 | 0.043 | 0.899 |  0.937 |  0.888 |  0.929 |  0.888 |  0.94  |  0.906 | 0.86  |
| PGAR       | 0.035 | 0.92  |  0.95  |  0.914 |  0.939 |  0.909 |  0.949 |  0.925 | 0.889 |
| DisenFuse  | 0.104 | 0.798 |  0.854 |  0.75  |  0.832 |  0.742 |  0.855 |  0.774 | 0.69  |
| DPANet     | 0.048 | 0.899 |  0.929 |  0.881 |  0.916 |  0.876 |  0.926 |  0.893 | 0.852 |
| ICNet      | 0.072 | 0.852 |  0.901 |  0.83  |  0.884 |  0.826 |  0.899 |  0.85  | 0.784 |
| D3Net      | 0.097 | 0.775 |  0.849 |  0.756 |  0.789 |  0.718 |  0.833 |  0.742 | 0.668 |
| RD3D       | 0.031 | 0.931 |  0.957 |  0.923 |  0.951 |  0.923 |  0.96  |  0.939 | 0.907 |
| CDCP       | 0.159 | 0.688 |  0.794 |  0.633 |  0.744 |  0.604 |  0.776 |  0.625 | 0.519 |
| CPFP       | 0.1   | 0.749 |  0.815 |  0.735 |  0.759 |  0.695 |  0.81  |  0.718 | 0.637 |
| CTMF       | 0.097 | 0.831 |  0.882 |  0.792 |  0.81  |  0.747 |  0.899 |  0.823 | 0.681 |
| DCMC       | 0.243 | 0.499 |  0.713 |  0.406 |  0.537 |  0.316 |  0.654 |  0.412 | 0.282 |
| DES        | 0.28  | 0.659 |  0.749 |  0.666 |  0.593 |  0.541 |  0.801 |  0.724 | 0.379 |
| DF         | 0.145 | 0.732 |  0.842 |  0.748 |  0.665 |  0.586 |  0.82  |  0.734 | 0.536 |
| DMRA       | 0.048 | 0.888 |  0.93  |  0.882 |  0.926 |  0.884 |  0.933 |  0.897 | 0.851 |
| MB         | 0.156 | 0.608 |  0.696 |  0.579 |  0.642 |  0.541 |  0.766 |  0.612 | 0.451 |
| MMCI       | 0.112 | 0.791 |  0.856 |  0.753 |  0.774 |  0.696 |  0.859 |  0.767 | 0.627 |
| NLPR       | 0.174 | 0.571 |  0.769 |  0.659 |  0.497 |  0.375 |  0.737 |  0.626 | 0.345 |
| PCANet     | 0.1   | 0.801 |  0.863 |  0.76  |  0.821 |  0.741 |  0.856 |  0.771 | 0.687 |
| TANet      | 0.093 | 0.808 |  0.871 |  0.779 |  0.83  |  0.761 |  0.861 |  0.79  | 0.704 |

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

<details>
<summary>
eval_unvos_method.py
</summary>

```python
# -*- coding: utf-8 -*-
import argparse
import os
import pickle
import warnings

import cv2
import numpy as np
import yaml
from joblib import Parallel, delayed
from prettytable import PrettyTable as ptable

from metrics.vos import f_boundary, jaccard

my_parser = argparse.ArgumentParser(
    description="The code is based on `https://github.com/davisvideochallenge/davis`",
    epilog="Enjoy the program! :)",
    allow_abbrev=False,
)
my_parser.version = "1.0.0"
my_parser.add_argument("-v", "--version", action="version")
my_parser.add_argument(
    "--name_list_path",
    default="/home/lart/Datasets/VideoSeg/DAVIS-2017-trainval-480p/DAVIS/ImageSets/2016/val.txt",
    type=str,
    help="the information file of DAVIS 2016 Dataset",
)
my_parser.add_argument(
    "--mask_root",
    default="/home/lart/Datasets/VideoSeg/DAVIS-2017-trainval-480p/DAVIS/Annotations/480p",
    type=str,
    help="the annotation folder of DAVIS 2016 Dataset",
)
my_parser.add_argument(
    "--pred_path",
    default="/home/lart/coding/USVideoSeg/output/HDFNet_WSGNR50_V1/pre",
    type=str,
    help="the prediction folder of the method",
)
my_parser.add_argument(
    "--save_path",
    default="./output/HDFNet_WSGNR50_V1.pkl",
    type=str,
    help="the file path for saving evaluation results",
)
my_parser.add_argument(
    "--ignore_head",
    default="True",
    choices=["True", "False"],
    type=str,
    help="whether to ignore the first frame during evaluation",
)
my_parser.add_argument(
    "--ignore_tail",
    default="True",
    choices=["True", "False"],
    type=str,
    help="whether to ignore the last frame during evaluation",
)
my_parser.add_argument(
    "--n_jobs",
    default=2,
    type=int,
    help="the number of jobs for parallel evaluating the performance",
)


def print_all_keys(data_dict, level: int = 0):
    level += 1
    if isinstance(data_dict, dict):
        for k, v in data_dict.items():
            print(f" {'|=' * level}>> {k}")
            print_all_keys(v, level=level)
    elif isinstance(data_dict, (list, tuple)):
        for item in data_dict:
            print_all_keys(item, level=level)
    else:
        return


def get_eval_video_name_list_from_yml(path: str, data_set: str) -> list:
    with open(path, encoding="utf-8", mode="r") as f_stream:
        data_info_dict = yaml.load(f_stream, Loader=yaml.FullLoader)

    eval_video_name_list = []
    for video_dict in data_info_dict["sequences"]:
        if video_dict["set"] == data_set:
            eval_video_name_list.append(video_dict["name"])
    return eval_video_name_list


def get_mean_recall_decay_for_video(per_frame_values):
    """Compute mean,recall and decay from per-frame evaluation.

    Arguments:
        per_frame_values (ndarray): per-frame evaluation

    Returns:
        M,O,D (float,float,float):
            return evaluation statistics: mean,recall,decay.
    """

    # strip off nan values
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", category=RuntimeWarning)
        M = np.nanmean(per_frame_values)
        O = np.nanmean(per_frame_values[1:-1] > 0.5)

    # Compute decay as implemented in Matlab
    per_frame_values = per_frame_values[1:-1]  # Remove first frame

    N_bins = 4
    ids = np.round(np.linspace(1, len(per_frame_values), N_bins + 1) + 1e-10) - 1
    ids = ids.astype(np.uint8)

    D_bins = [per_frame_values[ids[i]: ids[i + 1] + 1] for i in range(0, 4)]

    with warnings.catch_warnings():
        warnings.simplefilter("ignore", category=RuntimeWarning)
        D = np.nanmean(D_bins[0]) - np.nanmean(D_bins[3])

    return M, O, D


def _read_and_eval_file(mask_video_path: str, pred_video_path: str, frame_name: str):
    frame_mask_path = os.path.join(mask_video_path, frame_name)
    frame_pred_path = os.path.join(pred_video_path, frame_name)
    frame_mask = cv2.imread(frame_mask_path, 0)  # h, w
    frame_pred = cv2.imread(frame_pred_path, 0)
    binary_frame_mask = (frame_mask > 0).astype(np.float32)
    binary_frame_pred = (frame_pred > 0).astype(np.float32)
    J_score = jaccard.db_eval_iou(annotation=binary_frame_mask, segmentation=binary_frame_pred)
    F_score = f_boundary.db_eval_boundary(
        foreground_mask=binary_frame_pred, gt_mask=binary_frame_mask
    )
    return J_score, F_score


def _eval_video_sequence(
    method_pre_path: str,
    mask_data_root: str,
    video_name: str,
    ignore_head: bool,
    ignore_tail: bool,
):
    print(f"processing {video_name}...")

    mask_video_path = os.path.join(mask_data_root, video_name)
    pred_video_path = os.path.join(method_pre_path, video_name)

    mask_frame_path_list = sorted(os.listdir(mask_video_path))
    if ignore_head:
        mask_frame_path_list = mask_frame_path_list[1:]
    if ignore_tail:
        mask_frame_path_list = mask_frame_path_list[:-1]

    frame_score_list = [
        _read_and_eval_file(
            mask_video_path=mask_video_path,
            pred_video_path=pred_video_path,
            frame_name=frame_name,
        )
        for frame_name in mask_frame_path_list
    ]
    if ignore_head:
        frame_score_list = [[np.nan, np.nan]] + frame_score_list
    if ignore_tail:
        frame_score_list += [[np.nan, np.nan]]
    frame_score_array = np.asarray(frame_score_list)
    M, O, D = zip(
        *[
            get_mean_recall_decay_for_video(frame_score_array[:, i])
            for i in range(frame_score_array.shape[1])
        ]
    )
    return {
        video_name: {
            "pre_frame": frame_score_array,
            "mean": np.asarray(M),
            "recall": np.asarray(O),
            "decay": np.asarray(D),
        }
    }


def get_method_score_dict(
    method_pre_path: str,
    mask_data_root: str,
    video_name_list: list,
    ignore_head: bool = True,
    ignore_tail: bool = True,
    n_jobs: int = 2,
):
    video_score_list = Parallel(n_jobs=n_jobs)(
        delayed(_eval_video_sequence)(
            method_pre_path=method_pre_path,
            mask_data_root=mask_data_root,
            video_name=video_name,
            ignore_head=ignore_head,
            ignore_tail=ignore_tail,
        )
        for video_name in video_name_list
    )
    video_score_dict = {list(kv.keys())[0]: list(kv.values())[0] for kv in video_score_list}
    return video_score_dict


def get_method_average_score_dict(method_score_dict: dict):
    # average_score_dict = {"total": 0, "mean": 0, "recall": 0, "decay": 0}
    average_score_dict = {"Average": {"mean": 0, "recall": 0, "decay": 0}}
    for k, v in method_score_dict.items():
        # average_score_item = np.nanmean(v["pre_frame"], axis=0)
        # average_score_dict[k] = average_score_item
        average_score_dict[k] = {
            "mean": v["mean"],
            "recall": v["recall"],
            "decay": v["decay"],
        }
        # average_score_dict["total"] += average_score_item
        average_score_dict["Average"]["mean"] += v["mean"]
        average_score_dict["Average"]["recall"] += v["recall"]
        average_score_dict["Average"]["decay"] += v["decay"]
    # average_score_dict['Average']["total"] /= len(method_score_dict)
    average_score_dict["Average"]["mean"] /= len(method_score_dict)
    average_score_dict["Average"]["recall"] /= len(method_score_dict)
    average_score_dict["Average"]["decay"] /= len(method_score_dict)
    return average_score_dict


def save_to_file(data, save_path: str):
    with open(save_path, mode="wb") as f:
        pickle.dump(data, f)


def read_from_file(file_path: str):
    with open(file_path, mode="rb") as f:
        data = pickle.load(f)
    return data


def convert_data_dict_to_table(data_dict: dict, video_name_list: list):
    table = ptable(["Video", "J(M)", "J(O)", "J(D)", "F(M)", "F(O)", "F(D)"])
    for video_name in video_name_list:
        table.add_row(
            [video_name]
            + [
                f"{data_dict[video_name][x][y]: .3f}"
                for y in range(2)
                for x in ["mean", "recall", "decay"]
            ]
        )
    return "\n" + str(table) + "\n"


def get_eval_video_name_list_from_txt(path: str) -> list:
    name_list = []
    with open(path, encoding="utf-8", mode="r") as f:
        for line in f:
            line = line.strip()
            if line:
                name_list.append(line)
    return name_list


def eval_method_from_data(
    method_pre_path: str,
    mask_data_root: str,
    ignore_head: bool,
    ignore_tail: bool,
    name_list_path: str,
    save_path: str = "./output/average.pkl",
    n_jobs: int = 2,
):
    """
    根据给定方法的预测结果来评估在davis 2016上的性能
    :param method_pre_path: 模型预测结果，该路径下包含各个视频预测的结果，与Annotations文件夹布局一致
    :param mask_data_root: davis 2016的Annotations文件夹
    :param ignore_head: 评估时是否忽略第一帧
    :param ignore_tail: 评估时是否忽略最后一帧
    :param name_list_path: davis 2016数据集的信息文件（db_info.yml）或者是2017中提供的 2016/val.txt
    :param save_path: 保存导出的模型评估结果的文件路径
    :param n_jobs: 多进程评估时使用的进程数
    """
    if name_list_path.endswith(".yml") or name_list_path.endswith(".yaml"):
        # read yaml and get the list  that will be used to eval the model
        eval_video_name_list = get_eval_video_name_list_from_yml(
            path=name_list_path, data_set="test"
        )
    elif name_list_path.endswith(".txt"):
        eval_video_name_list = get_eval_video_name_list_from_txt(path=name_list_path)
    else:
        raise ValueError

    # tervese the each video
    method_score_dict = get_method_score_dict(
        method_pre_path=method_pre_path,
        mask_data_root=mask_data_root,
        video_name_list=eval_video_name_list,
        ignore_head=ignore_head,
        ignore_tail=ignore_tail,
        n_jobs=n_jobs,
    )
    # get the average score
    average_score_dict = get_method_average_score_dict(method_score_dict=method_score_dict)

    if save_path != None:
        save_to_file(data=average_score_dict, save_path=save_path)

    # show the results
    eval_video_name_list += ["Average"]
    table_str = convert_data_dict_to_table(
        data_dict=average_score_dict, video_name_list=eval_video_name_list
    )
    print(table_str)


def show_results_from_data_file(file_path: str = "./output/average.pkl"):
    """
    展示给定的模型评估结果文件中包含的模型的结果
    :param file_path: 保存导出的模型评估结果的文件路径
    """
    average_score_dict = read_from_file(file_path=file_path)

    eval_video_name_list = list(average_score_dict.keys())
    eval_video_name_list[0], eval_video_name_list[-1] = (
        eval_video_name_list[-1],
        eval_video_name_list[0],
    )
    # show the results
    table_str = convert_data_dict_to_table(
        data_dict=average_score_dict, video_name_list=eval_video_name_list
    )
    print(table_str)


if __name__ == "__main__":
    args = my_parser.parse_args()
    eval_method_from_data(
        method_pre_path=args.pred_path,
        mask_data_root=args.mask_root,
        ignore_tail=True if args.ignore_tail == "True" else False,
        ignore_head=True if args.ignore_head == "True" else False,
        name_list_path=args.name_list_path,
        save_path=args.save_path,
        n_jobs=args.n_jobs,
    )
    # show_results_from_data_file("./output/dybinary_ave.pkl")
    # show_results_from_data_file("./output/HDFNet_WSGNR50_V1.pkl")
    # show_results_from_data_file("./output/matnet_ave.pkl")
```

</details>
