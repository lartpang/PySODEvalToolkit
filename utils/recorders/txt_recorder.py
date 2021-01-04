# -*- coding: utf-8 -*-
# @Time    : 2021/1/4
# @Author  : Lart Pang
# @GitHub  : https://github.com/lartpang

from datetime import datetime


class TxtRecorder:
    def __init__(self, txt_path, resume=True):
        self.txt_path = txt_path
        mode = "a" if resume else "w"
        with open(txt_path, mode=mode, encoding="utf-8") as f:
            f.write(f" ========>> Date: {datetime.now()} <<======== \n")

    def add_row(self, row_name, row_data):
        with open(self.txt_path, mode="a", encoding="utf-8") as f:
            f.write(f" ========>> {row_name}: {row_data} <<======== \n")

    def add_method_results(self, data_dict: dict, method_name: str = ""):
        # save the results under testing
        msg = method_name
        for k, v in data_dict.items():
            msg += f" {k} {v}\n"
        with open(self.txt_path, mode="a", encoding="utf-8") as f:
            f.write(msg + "\n")
