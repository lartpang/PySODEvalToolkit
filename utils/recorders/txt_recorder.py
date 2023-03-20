# -*- coding: utf-8 -*-
# @Time    : 2021/1/4
# @Author  : Lart Pang
# @GitHub  : https://github.com/lartpang

from datetime import datetime


class TxtRecorder:
    def __init__(self, txt_path, to_append=True, max_method_name_width=10):
        """
        用于向txt文档写数据的类。

        :param txt_path: txt文档路径
        :param to_append: 是否要继续使用之前的文档，如果没有就重新创建
        :param max_method_name_width: 方法字符串的最大长度
        """
        self.txt_path = txt_path
        self.max_method_name_width = max_method_name_width
        mode = "a" if to_append else "w"
        with open(txt_path, mode=mode, encoding="utf-8") as f:
            f.write(f"\n ========>> Date: {datetime.now()} <<======== \n")
        self.row_names = []

    def add_row(self, row_name, row_data, row_start_str="", row_end_str="\n"):
        self.row_names.append(row_name)
        with open(self.txt_path, mode="a", encoding="utf-8") as f:
            f.write(f"{row_start_str} ========>> {row_name}: {row_data} <<======== {row_end_str}")

    def __call__(
        self,
        method_results: dict,
        method_name: str = "",
        row_start_str="",
        row_end_str="\n",
        value_width=6,
    ):
        msg = row_start_str
        if len(method_name) > self.max_method_name_width:
            method_name = method_name[: self.max_method_name_width - 3] + "..."
        else:
            method_name += " " * (self.max_method_name_width - len(method_name))
        msg += f"[{method_name}] "
        for metric_name, metric_value in method_results.items():
            assert isinstance(metric_value, float)
            msg += f"{metric_name}: "
            real_width = len(str(metric_value))
            if value_width > real_width:
                # 后补空格
                msg += f"{metric_value}" + " " * (value_width - real_width)
            else:
                # 真实数据长度超过了限定，这时需要近似保留小数
                # 保留指定位数，注意，这里由于数据都是0~1之间的数据，所以使用round的时候需要去掉前面的`0.`
                msg += f"{round(metric_value, ndigits=value_width - 2)}"
            msg += " "
        msg += row_end_str
        with open(self.txt_path, mode="a", encoding="utf-8") as f:
            f.write(msg)
