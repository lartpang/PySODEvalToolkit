# -*- coding: utf-8 -*-
import numpy as np
from py_sod_metrics.sod_metrics import _TYPE, _prepare_data


class ExtraSegMeasure(object):
    def __init__(self):
        self.precisions = []
        self.recalls = []
        self.specificities = []
        self.dices = []
        self.fmeasures = []
        self.ious = []

    def step(self, pred: np.ndarray, gt: np.ndarray):
        pred, gt = _prepare_data(pred, gt)

        precisions, recalls, specificities, dices, fmeasures, ious = self.cal_metrics(
            pred=pred, gt=gt
        )

        self.precisions.append(precisions)
        self.recalls.append(recalls)
        self.specificities.append(specificities)
        self.dices.append(dices)
        self.fmeasures.append(fmeasures)
        self.ious.append(ious)

    def cal_metrics(self, pred: np.ndarray, gt: np.ndarray) -> tuple:
        """
        Calculate the corresponding precision and recall when the threshold changes from 0 to 255.

        These precisions and recalls can be used to obtain the mean F-measure, maximum F-measure,
        precision-recall curve and F-measure-threshold curve.

        For convenience, ``changeable_fms`` is provided here, which can be used directly to obtain
        the mean F-measure, maximum F-measure and F-measure-threshold curve.

        IoU = NumAnd / (FN + NumRec)
        PreFtem = NumAnd / NumRec
        RecallFtem = NumAnd / num_obj
        SpecifTem = TN / (TN + FP)
        Dice = 2 * NumAnd / (num_obj + num_pred)
        FmeasureF = (2.0 * PreFtem * RecallFtem) / (PreFtem + RecallFtem)

        :return: precisions, recalls, specificities, dices, fmeasures, ious
        """
        # 1. 获取预测结果在真值前背景区域中的直方图
        pred: np.ndarray = (pred * 255).astype(np.uint8)
        bins: np.ndarray = np.linspace(0, 256, 257)
        tp_hist, _ = np.histogram(pred[gt], bins=bins)  # 最后一个bin为[255, 256]
        fp_hist, _ = np.histogram(pred[~gt], bins=bins)
        # 2. 使用累积直方图（Cumulative Histogram）获得对应真值前背景中大于不同阈值的像素数量
        # 这里使用累加（cumsum）就是为了一次性得出 >=不同阈值 的像素数量, 这里仅计算了前景区域
        tp_w_thrs = np.cumsum(np.flip(tp_hist), axis=0)
        fp_w_thrs = np.cumsum(np.flip(fp_hist), axis=0)
        # 3. 使用不同阈值的结果计算对应的precision和recall
        # p和r的计算的真值是pred==1&gt==1，二者仅有分母不同，分母前者是pred==1，后者是gt==1
        # 为了同时计算不同阈值的结果，这里使用hsitogram&flip&cumsum 获得了不同各自的前景像素数量
        TPs = tp_w_thrs
        FPs = fp_w_thrs
        T = np.count_nonzero(gt)  # T=TPs+FNs
        FNs = T - TPs
        Ps = TPs + FPs  # p_w_thrs
        Ns = pred.size - Ps
        TNs = Ns - FNs

        ious = np.where(Ps + FNs == 0, 0, TPs / (Ps + FNs))
        specificities = np.where(TNs + FPs == 0, 0, TNs / (TNs + FPs))
        dices = np.where(TPs + FPs == 0, 0, 2 * TPs / (T + Ps))
        precisions = np.where(Ps == 0, 0, TPs / Ps)
        recalls = np.where(TPs == 0, 0, TPs / T)
        fmeasures = np.where(
            precisions + recalls == 0, 0, (2 * precisions * recalls) / (precisions + recalls)
        )
        return precisions, recalls, specificities, dices, fmeasures, ious

    def get_results(self) -> dict:
        """
        Return the results about F-measure.

        :return: dict(fm=dict(adp=adaptive_fm, curve=changeable_fm), pr=dict(p=precision, r=recall))
        """
        precision = np.mean(np.array(self.precisions, dtype=_TYPE), axis=0)
        recall = np.mean(np.array(self.recalls, dtype=_TYPE), axis=0)
        specificitiy = np.mean(np.array(self.specificities, dtype=_TYPE), axis=0)
        fmeasure = np.mean(np.array(self.fmeasures, dtype=_TYPE), axis=0)
        dice = np.mean(np.array(self.dices, dtype=_TYPE), axis=0)
        iou = np.mean(np.array(self.ious, dtype=_TYPE), axis=0)
        return dict(pre=precision, sen=recall, spec=specificitiy, fm=fmeasure, dice=dice, iou=iou)
