# -*- coding: utf-8 -*-
# @Time    : 2021/1/4
# @Author  : Lart Pang
# @GitHub  : https://github.com/lartpang
import math

import matplotlib.pyplot as plt
import numpy as np

from utils.misc import update_info


class CurveDrawer(object):
    def __init__(
        self,
        row_num,
        num_subplots,
        font_cfg=None,
        subplots_cfg=None,
        separated_legend=False,
        sharey=True,
    ):
        self.separated_legend = separated_legend
        if self.separated_legend:
            num_subplots += 1
        self.num_subplots = num_subplots
        self.sharey = sharey

        fig, axes = plt.subplots(
            nrows=row_num,
            ncols=math.ceil(self.num_subplots / row_num),
            sharey=self.sharey,
        )
        self.fig = fig
        self.axes = axes.flatten()

        if subplots_cfg is None:
            subplots_cfg = dict(
                left=None, bottom=None, right=None, top=None, wspace=None, hspace=None
            )
        self.subplots_cfg = subplots_cfg

        self.font_cfg = {
            "title": {
                "fontdict": {
                    "fontsize": 12,
                    "fontweight": "bold",
                }
            },
            "label": {
                "fontdict": {
                    "fontsize": 10,
                    "fontweight": "normal",
                }
            },
            "ticks": {
                "fontdict": {
                    "fontsize": 8,
                    "fontweight": "normal",
                }
            },
            "legend": {
                "ncol": 1,
                "prop": {
                    "size": 8,
                    "weight": "normal",
                },
            },
        }
        if font_cfg is not None:
            update_info(source_info=self.font_cfg, new_info=font_cfg)

        self.init_subplots()
        self.dummy_data = {}

    def init_subplots(self):
        plt.style.use("default")
        plt.subplots_adjust(**self.subplots_cfg)
        for ax in self.axes:
            ax.grid(False)
            ax.set_axis_off()
        print(f"Config: {self.subplots_cfg}\n{self.font_cfg}")

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
        # [CPFP, "red", "-", "OURS", 3],
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
        self, idx, title=None, x_label=None, y_label=None, x_lim=None, y_lim=None
    ):
        ax = self.axes[idx]

        ax.grid(True)
        ax.set_axis_on()

        # give plot a title
        ax.set_title(title, **self.font_cfg["title"])

        # make axis labels
        ax.set_xlabel(x_label, **self.font_cfg["label"])
        ax.set_ylabel(y_label, **self.font_cfg["label"])

        # 对坐标刻度的设置
        ax.set_xlim(x_lim)
        ax.set_ylim(y_lim)

        if x_lim is not None:
            x_ticks = np.linspace(min(x_lim), max(x_lim), 11)
        else:
            x_ticks = []
        if y_lim is not None:
            y_ticks = np.linspace(min(y_lim), max(y_lim), 11)
        else:
            y_ticks = []

        ax.set_xticks(x_ticks)
        ax.set_yticks(y_ticks)
        ax.set_xticklabels(labels=[f"{x:.1f}" for x in x_ticks], **self.font_cfg["ticks"])
        ax.set_yticklabels(labels=[f"{y:.2f}" for y in y_ticks], **self.font_cfg["ticks"])

        # 对坐标轴的框线进行设置, 设置轴
        ax.spines["top"].set_linewidth(1)
        ax.spines["bottom"].set_linewidth(1)
        ax.spines["left"].set_linewidth(1)
        ax.spines["right"].set_linewidth(1)

    def show(self):
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
            ax.grid(False)
            ax.set_axis_off()
            ax.legend(loc=3, **self.font_cfg["legend"])
        else:
            # settings for the legneds of all common subplots.
            for ax in self.axes:
                # loc=0，自动将位置放在最合适的
                ax.legend(loc=3, **self.font_cfg["legend"])
        plt.show()
