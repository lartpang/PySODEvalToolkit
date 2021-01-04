# -*- coding: utf-8 -*-
# @Time    : 2021/1/4
# @Author  : Lart Pang
# @GitHub  : https://github.com/lartpang

import matplotlib.pyplot as plt
import numpy as np


class CurveDrawer:
    def __init__(self, row_num, col_num):
        self.fig = plt.figure()
        self.row_num = row_num
        self.col_num = col_num
        self.font_cfg = {
            "title": {
                "fontsize": 12,
                "fontweight": "bold",
                "fontname": "Liberation Sans",
            },
            "label": {
                "fontsize": 10,
                "fontweight": "normal",
                "fontname": "Liberation Sans",
            },
            "ticks": {
                "fontsize": 8,
                "fontweight": "normal",
                "fontname": "Liberation Sans",
            },
            "legend": {
                "size": 8,
                "weight": "normal",
                "family": "Liberation Sans",
            },
        }

    def add_subplot(self, curr_idx):
        assert isinstance(curr_idx, int) and curr_idx > 0
        self.ax = self.fig.add_subplot(self.row_num, self.col_num, curr_idx)
        self.ax.grid(True)

    def draw_method_curve(
        self,
        dataset_name,
        method_curve_setting,
        x_label,
        y_label,
        x_data,
        y_data,
        x_lim: tuple = (0, 1),
        y_lim: tuple = (0.1, 1),
    ):
        """
        :param method_curve_setting:  {
                "line_color": "color"(str),
                "line_style": "style"(str),
                "line_label": "label"(str),
                "line_width": width(int),
            }
        """
        # give plot a title
        self.ax.set_title(dataset_name, fontdict=self.font_cfg["title"])

        # make axis labels
        self.ax.set_xlabel(x_label, fontdict=self.font_cfg["label"])
        self.ax.set_ylabel(y_label, fontdict=self.font_cfg["label"])

        # 对坐标刻度的设置
        label = [f"{x:.2f}" for x in np.linspace(0, 1, 11)]
        self.ax.set_xticks(np.linspace(0, 1, 11))
        self.ax.set_yticks(np.linspace(0, 1, 11))
        self.ax.set_xticklabels(labels=label, fontdict=self.font_cfg["ticks"])
        self.ax.set_yticklabels(labels=label, fontdict=self.font_cfg["ticks"])

        self.ax.set_xlim(x_lim)
        self.ax.set_ylim(y_lim)

        # [CPFP, "red", "-", "OURS", 3],
        self.ax.plot(
            x_data,
            y_data,
            linewidth=method_curve_setting["line_width"],
            label=method_curve_setting["line_label"],
            color=method_curve_setting["line_color"],
            linestyle=method_curve_setting["line_style"],
        )

        # loc=0，自动将位置放在最合适的
        self.ax.legend(loc=3, prop=self.font_cfg["legend"])

        # 对坐标轴的框线进行设置, 设置轴
        self.ax.spines["top"].set_linewidth(1)
        self.ax.spines["bottom"].set_linewidth(1)
        self.ax.spines["left"].set_linewidth(1)
        self.ax.spines["right"].set_linewidth(1)

    def show(self):
        plt.show()
