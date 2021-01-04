# -*- coding: utf-8 -*-
# @Time    : 2021/1/4
# @Author  : Lart Pang
# @GitHub  : https://github.com/lartpang

import numpy as np

from metrics.sod.metrics import MAE, Emeasure, Fmeasure, Smeasure, WeightedFmeasure


class MetricRecorder(object):
    def __init__(self):
        self.mae = MAE()
        self.fm = Fmeasure()
        self.sm = Smeasure()
        self.em = Emeasure()
        self.wfm = WeightedFmeasure()

    def update(self, pre: np.ndarray, gt: np.ndarray):
        assert pre.dtype == np.uint8, pre.dtype
        assert gt.dtype == np.uint8, gt.dtype

        self.mae.step(pre, gt)
        self.sm.step(pre, gt)
        self.fm.step(pre, gt)
        self.em.step(pre, gt)
        self.wfm.step(pre, gt)

    def show(self, bit_num=3) -> dict:
        fm_info = self.fm.get_results()
        fm = fm_info["fm"]
        pr = fm_info["pr"]
        wfm = self.wfm.get_results()["wfm"]
        sm = self.sm.get_results()["sm"]
        em = self.em.get_results()["em"]
        mae = self.mae.get_results()["mae"]
        results = {
            "em": em["curve"],
            "fm": fm["curve"],
            "p": pr["p"],
            "r": pr["r"],
            "Sm": sm,
            "wFm": wfm,
            "MAE": mae,
            "adpEm": em["adp"],
            "adpFm": fm["adp"],
        }
        if isinstance(bit_num, int):
            results = {k: v.round(bit_num) for k, v in results.items()}
        return results
