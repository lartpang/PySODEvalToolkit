# -*- coding: utf-8 -*-
# @Time    : 2021/1/4
# @Author  : Lart Pang
# @GitHub  : https://github.com/lartpang
import math
import os

import matplotlib.pyplot as plt
import numpy as np


class CurveDrawer(object):
    def __init__(
        self,
        row_num,
        num_subplots,
        style_cfg=None,
        ncol_of_legend=1,
        separated_legend=False,
        sharey=False,
    ):
        """A better wrapper of matplotlib for me.

        Args:
            row_num (int): Number of rows.
            num_subplots (int): Number of subplots.
            style_cfg (str, optional): Style yaml file path for matplotlib. Defaults to None.
            ncol_of_legend (int, optional): Number of columns of the legend. Defaults to 1.
            separated_legend (bool, optional): Use the separated legend. Defaults to False.
            sharey (bool, optional): Use a shared y-axis. Defaults to False.
        """
        if style_cfg is not None:
            assert os.path.isfile(style_cfg)
            plt.style.use(style_cfg)

        self.ncol_of_legend = ncol_of_legend
        self.separated_legend = separated_legend
        if self.separated_legend:
            num_subplots += 1
        self.num_subplots = num_subplots
        self.sharey = sharey

        fig, axes = plt.subplots(
            nrows=row_num, ncols=math.ceil(self.num_subplots / row_num), sharey=self.sharey
        )
        self.fig = fig
        self.axes = axes
        if isinstance(self.axes, np.ndarray):
            self.axes = self.axes.flatten()
        else:
            self.axes = [self.axes]

        self.init_subplots()
        self.dummy_data = {}

    def init_subplots(self):
        for ax in self.axes:
            ax.set_axis_off()

    def plot_at_axis(self, idx, method_curve_setting, x_data, y_data):
        """
        :param method_curve_setting:  {
                "line_color": "color"(str),
                "line_style": "style"(str),
                "line_label": "label"(str),
                "line_width": width(int),
            }
        """
        assert isinstance(idx, int) and 0 <= idx < self.num_subplots
        self.axes[idx].plot(
            x_data,
            y_data,
            linewidth=method_curve_setting["line_width"],
            label=method_curve_setting["line_label"],
            color=method_curve_setting["line_color"],
            linestyle=method_curve_setting["line_style"],
        )

        if self.separated_legend:
            self.dummy_data[method_curve_setting["line_label"]] = method_curve_setting

    def set_axis_property(
        self, idx, title=None, x_label=None, y_label=None, x_ticks=None, y_ticks=None
    ):
        ax = self.axes[idx]

        ax.set_axis_on()

        # give plot a title
        ax.set_title(title)

        # make axis labels
        ax.set_xlabel(x_label)
        ax.set_ylabel(y_label)

        # 对坐标刻度的设置
        x_ticks = [] if x_ticks is None else x_ticks
        y_ticks = [] if y_ticks is None else y_ticks
        ax.set_xlim((min(x_ticks), max(x_ticks)))
        ax.set_ylim((min(y_ticks), max(x_ticks)))
        ax.set_xticks(x_ticks)
        ax.set_yticks(y_ticks)
        ax.set_xticklabels(labels=[f"{x:.2f}" for x in x_ticks])
        ax.set_yticklabels(labels=[f"{y:.2f}" for y in y_ticks])

    def _plot(self):
        if self.sharey:
            for ax in self.axes[1:]:
                ax.set_ylabel(None)
                ax.tick_params(bottom=True, top=False, left=False, right=False)

        if self.separated_legend:
            # settings for the legend axis
            for method_label, method_info in self.dummy_data.items():
                self.plot_at_axis(
                    idx=self.num_subplots - 1, method_curve_setting=method_info, x_data=0, y_data=0
                )
            ax = self.axes[self.num_subplots - 1]
            ax.set_axis_off()
            ax.legend(loc=10, ncol=self.ncol_of_legend, facecolor="white", edgecolor="white")
        else:
            # settings for the legneds of all common subplots.
            for ax in self.axes:
                # loc=0，自动将位置放在最合适的
                ax.legend(loc=3, ncol=self.ncol_of_legend, facecolor="white", edgecolor="white")

    def show(self):
        self._plot()
        plt.tight_layout()
        plt.show()

    def save(self, path):
        self._plot()
        plt.tight_layout()
        plt.savefig(path)
