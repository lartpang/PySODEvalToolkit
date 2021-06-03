# -*- coding: utf-8 -*-
# @Time    : 2021/4/24
# @Author  : Lart Pang
# @GitHub  : https://github.com/lartpang

import glob
import os
import re
import shutil


def path_join(base_path, sub_path):
    if sub_path.startswith(os.sep):
        sub_path = sub_path[len(os.sep) :]
    return os.path.join(base_path, sub_path)


def rename_all_files(src_pattern, dst_pattern, src_name, src_dir, dst_dir=None):
    """
    :param src_pattern: 匹配原始数据名字的正则表达式
    :param dst_pattern: 对应的修改后的字符式
    :param src_dir: 存放原始数据的文件夹路径，可以组合src_name来构造路径模式，使用glob进行数据搜索
    :param src_name: glob类型的模式
    :param dst_dir: 存放修改后数据的文件夹路径，默认为None，表示直接修改原始数据
    """
    assert os.path.isdir(src_dir)

    if dst_dir is None:
        dst_dir = src_dir
        rename_func = os.replace
    else:
        assert os.path.isdir(dst_dir)
        if dst_dir == src_dir:
            rename_func = os.replace
        else:
            rename_func = shutil.copy
    print(f"将会使用 {rename_func.__name__} 来修改数据")

    src_dir = os.path.abspath(src_dir)
    dst_dir = os.path.abspath(dst_dir)
    src_data_paths = glob.glob(path_join(src_dir, src_name))

    print(f"开始替换 {src_dir} 中的数据")
    for idx, src_data_path in enumerate(src_data_paths, start=1):
        src_name_w_dir_name = src_data_path[len(src_dir) + 1 :]
        dst_name_w_dir_name = re.sub(src_pattern, repl=dst_pattern, string=src_name_w_dir_name)
        if dst_name_w_dir_name == src_name_w_dir_name:
            continue
        dst_data_path = path_join(dst_dir, dst_name_w_dir_name)

        dst_data_dir = os.path.dirname(dst_data_path)
        if not os.path.exists(dst_data_dir):
            print(f"{idx}: {dst_data_dir} 不存在，新建一下")
            os.makedirs(dst_data_dir)
        rename_func(src=src_data_path, dst=dst_data_path)
        print(f"{src_data_path} -> {dst_data_path}")

    print("OK...")


if __name__ == "__main__":
    rename_all_files(
        src_pattern=r"",
        dst_pattern="",
        src_name="*/*.png",
        src_dir="",
        dst_dir="",
    )
