# -*- coding: utf-8 -*-
# @Time    : 2021/1/4
# @Author  : Lart Pang
# @GitHub  : https://github.com/lartpang
from collections import defaultdict

import numpy as np
from py_sod_metrics.sod_metrics import (
    MAE,
    Emeasure,
    Fmeasure,
    Smeasure,
    WeightedFmeasure,
)


def ndarray_to_basetype(data):
    """
    将单独的ndarray，或者tuple，list或者dict中的ndarray转化为基本数据类型，
    即列表(.tolist())和python标量
    """

    def _to_list_or_scalar(item):
        listed_item = item.tolist()
        if isinstance(listed_item, list) and len(listed_item) == 1:
            listed_item = listed_item[0]
        return listed_item

    if isinstance(data, (tuple, list)):
        results = [_to_list_or_scalar(item) for item in data]
    elif isinstance(data, dict):
        results = {k: _to_list_or_scalar(item) for k, item in data.items()}
    else:
        assert isinstance(data, np.ndarray)
        results = _to_list_or_scalar(data)
    return results


class MetricRecorder(object):
    def __init__(self):
        """
        用于统计各种指标的类
        """
        self.mae = MAE()
        self.fm = Fmeasure()
        self.sm = Smeasure()
        self.em = Emeasure()
        self.wfm = WeightedFmeasure()

    def update(self, pre: np.ndarray, gt: np.ndarray):
        assert pre.shape == gt.shape
        assert pre.dtype == np.uint8
        assert gt.dtype == np.uint8

        self.mae.step(pre, gt)
        self.sm.step(pre, gt)
        self.fm.step(pre, gt)
        self.em.step(pre, gt)
        self.wfm.step(pre, gt)

    def show(self, num_bits: int = 3, return_ndarray: bool = False) -> dict:
        """
        返回指标计算结果：

        - 曲线数据(sequential)： fm/em/p/r
        - 数值指标(numerical)： SM/MAE/maxE/avgE/adpE/maxF/avgF/adpF/wFm
        """
        fm_info = self.fm.get_results()
        fm = fm_info["fm"]
        pr = fm_info["pr"]
        wfm = self.wfm.get_results()["wfm"]
        sm = self.sm.get_results()["sm"]
        em = self.em.get_results()["em"]
        mae = self.mae.get_results()["mae"]

        sequential_results = {
            "fm": np.flip(fm["curve"]),
            "em": np.flip(em["curve"]),
            "p": np.flip(pr["p"]),
            "r": np.flip(pr["r"]),
        }
        numerical_results = {
            "SM": sm,
            "MAE": mae,
            "maxE": em["curve"].max(),
            "avgE": em["curve"].mean(),
            "adpE": em["adp"],
            "maxF": fm["curve"].max(),
            "avgF": fm["curve"].mean(),
            "adpF": fm["adp"],
            "wFm": wfm,
        }
        if num_bits is not None and isinstance(num_bits, int):
            numerical_results = {k: v.round(num_bits) for k, v in numerical_results.items()}
        if not return_ndarray:
            sequential_results = ndarray_to_basetype(sequential_results)
            numerical_results = ndarray_to_basetype(numerical_results)
        return {"sequential": sequential_results, "numerical": numerical_results}


class GroupedMetricRecorder(object):
    def __init__(self):
        self.metric_recorders = {}
        # 这些指标会根据最终所有分组进行平均得到的曲线计算
        self.re_cal_metrics = ["maxE", "avgE", "maxF", "avgF"]

    def update(self, group_name: str, pre: np.ndarray, gt: np.ndarray):
        if group_name not in self.metric_recorders:
            self.metric_recorders[group_name] = MetricRecorder()
        self.metric_recorders[group_name].update(pre, gt)

    def show(self, num_bits: int = 3, return_ndarray: bool = False) -> dict:
        """
        返回指标计算结果：

        - 曲线数据(sequential)： fm/em/p/r
        - 数值指标(numerical)： SM/MAE/maxE/avgE/adpE/maxF/avgF/adpF/wFm
        """
        group_metrics = {}
        for k, v in self.metric_recorders.items():
            group_metric = v.show(num_bits=None, return_ndarray=True)
            group_metrics[k] = {
                **group_metric["sequential"],
                **{
                    metric_name: metric_value
                    for metric_name, metric_value in group_metric["numerical"].items()
                    if metric_name not in self.re_cal_metrics
                },
            }
        avg_results = self.average_group_metrics(group_metrics=group_metrics)

        sequential_results = {
            "fm": avg_results["fm"],
            "em": avg_results["em"],
            "p": avg_results["p"],
            "r": avg_results["r"],
        }
        numerical_results = {
            "SM": avg_results["SM"],
            "MAE": avg_results["MAE"],
            "maxE": avg_results["em"].max(),
            "avgE": avg_results["em"].mean(),
            "adpE": avg_results["adpE"],
            "maxF": avg_results["fm"].max(),
            "avgF": avg_results["fm"].mean(),
            "adpF": avg_results["adpF"],
            "wFm": avg_results["wFm"],
        }
        if num_bits is not None and isinstance(num_bits, int):
            numerical_results = {k: v.round(num_bits) for k, v in numerical_results.items()}
        if not return_ndarray:
            sequential_results = ndarray_to_basetype(sequential_results)
            numerical_results = ndarray_to_basetype(numerical_results)
        return {"sequential": sequential_results, "numerical": numerical_results}

    @staticmethod
    def average_group_metrics(group_metrics: dict) -> dict:
        recorder = defaultdict(list)
        for group_name, metrics in group_metrics.items():
            for metric_name, metric_array in metrics.items():
                recorder[metric_name].append(metric_array)
        results = {k: np.mean(np.vstack(v), axis=0) for k, v in recorder.items()}
        return results
