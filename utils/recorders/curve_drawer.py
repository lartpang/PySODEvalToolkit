# -*- coding: utf-8 -*-
# @Time    : 2021/1/4
# @Author  : Lart Pang
# @GitHub  : https://github.com/lartpang

import matplotlib.pyplot as plt
import numpy as np


class CurveDrawer(object):
    def __init__(self, row_num, col_num):
        fig, axes = plt.subplots(nrows=row_num, ncols=col_num)
        self.fig = fig
        self.axes = axes.flatten()

        self.num_subplots = row_num * col_num
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

        self.init_subplots()

    def init_subplots(self):
        plt.style.use("default")
        for ax in self.axes:
            ax.grid(False)
            ax.set_axis_off()

    def draw_method_curve(
        self,
        curr_idx,
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
        assert isinstance(curr_idx, int) and 0 <= curr_idx < self.num_subplots
        ax = self.axes[curr_idx]
        ax.grid(True)
        ax.set_axis_on()

        # give plot a title
        ax.set_title(dataset_name, fontdict=self.font_cfg["title"])

        # make axis labels
        ax.set_xlabel(x_label, fontdict=self.font_cfg["label"])
        ax.set_ylabel(y_label, fontdict=self.font_cfg["label"])

        # 对坐标刻度的设置
        label = [f"{x:.2f}" for x in np.linspace(0, 1, 11)]
        ax.set_xticks(np.linspace(0, 1, 11))
        ax.set_yticks(np.linspace(0, 1, 11))
        ax.set_xticklabels(labels=label, fontdict=self.font_cfg["ticks"])
        ax.set_yticklabels(labels=label, fontdict=self.font_cfg["ticks"])

        ax.set_xlim(x_lim)
        ax.set_ylim(y_lim)

        # [CPFP, "red", "-", "OURS", 3],
        ax.plot(
            x_data,
            y_data,
            linewidth=method_curve_setting["line_width"],
            label=method_curve_setting["line_label"],
            color=method_curve_setting["line_color"],
            linestyle=method_curve_setting["line_style"],
        )

        # loc=0，自动将位置放在最合适的
        ax.legend(loc=3, prop=self.font_cfg["legend"])

        # 对坐标轴的框线进行设置, 设置轴
        ax.spines["top"].set_linewidth(1)
        ax.spines["bottom"].set_linewidth(1)
        ax.spines["left"].set_linewidth(1)
        ax.spines["right"].set_linewidth(1)

    def show(self):
        plt.show()


if __name__ == "__main__":
    drawer = OldCurveDrawer(4, 4)
