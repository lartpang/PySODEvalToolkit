# -*- coding: utf-8 -*-
import glob
import os
import re

import cv2
import numpy as np


def get_ext(path_list):
    ext_list = list(set([os.path.splitext(p)[1] for p in path_list]))
    if len(ext_list) != 1:
        if ".png" in ext_list:
            ext = ".png"
        elif ".jpg" in ext_list:
            ext = ".jpg"
        elif ".bmp" in ext_list:
            ext = ".bmp"
        else:
            raise NotImplementedError
        print(f"预测文件夹中包含多种扩展名，这里仅使用{ext}")
    else:
        ext = ext_list[0]
    return ext


def get_name_list_and_suffix(data_path: str) -> tuple:
    name_list = []
    if os.path.isfile(data_path):
        print(f" ++>> {data_path} is a file. <<++ ")
        with open(data_path, mode="r", encoding="utf-8") as file:
            line = file.readline()
            while line:
                img_name = os.path.basename(line.split()[0])
                file_ext = os.path.splitext(img_name)[1]
                name_list.append(os.path.splitext(img_name)[0])
                line = file.readline()
        if file_ext == "":
            # 默认为png
            file_ext = ".png"
    else:
        print(f" ++>> {data_path} is a folder. <<++ ")
        data_list = os.listdir(data_path)
        file_ext = get_ext(data_list)
        name_list = [os.path.splitext(f)[0] for f in data_list if f.endswith(file_ext)]
    name_list = list(set(name_list))
    return name_list, file_ext


def get_name_list(data_path: str, name_prefix: str = "", name_suffix: str = "") -> list:
    if os.path.isfile(data_path):
        assert data_path.endswith((".txt", ".lst"))
        data_list = []
        with open(data_path, encoding="utf-8", mode="r") as f:
            line = f.readline().strip()
            while line:
                data_list.append(line)
                line = f.readline().strip()
    else:
        data_list = os.listdir(data_path)

    name_list = data_list
    if not name_prefix and not name_suffix:
        name_list = [os.path.splitext(f)[0] for f in name_list]
    else:
        name_list = [
            f[len(name_prefix) : -len(name_suffix)]
            for f in name_list
            if f.startswith(name_prefix) and f.endswith(name_suffix)
        ]

    name_list = list(set(name_list))
    return name_list


def get_number_from_tail(string):
    tail_number = re.findall(pattern="\d+$", string=string)[0]
    return int(tail_number)


def get_name_with_group_list(
    data_path: str,
    name_prefix: str = "",
    name_suffix: str = "",
    start_idx: int = 0,
    end_idx: int = None,
    sep: str = "<sep>",
):
    """get file names with the group name

    Args:
        data_path (str): The path of data.
        name_prefix (str, optional): The prefix of the file name. Defaults to "".
        name_suffix (str, optional): The suffix of the file name. Defaults to "".
        start_idx (int, optional): The index of the first frame in each group. Defaults to 0, it will not skip any frames.
        end_idx (int, optional): The index of the last frame in each group. Defaults to None, it will not skip any frames.
        sep (str, optional): The returned name is a string containing group_name and file_name separated by `sep`.

    Raises:
        NotImplementedError: Undefined.

    Returns:
        list: The name (with the group name) list and the original number of image in the dataset.
    """
    name_list = []
    if os.path.isfile(data_path):
        # 暂未遇到类似的设定
        raise NotImplementedError
    else:
        if "*" in data_path:  # for VCOD
            group_paths = glob.glob(data_path, recursive=False)
            group_name_start_idx = data_path.find("*")
            for group_path in group_paths:
                group_name = group_path[group_name_start_idx:].split(os.sep)[0]

                file_names = sorted(
                    [
                        n[len(name_prefix) : -len(name_suffix)]
                        for n in os.listdir(group_path)
                        if n.startswith(name_prefix) and n.endswith(name_suffix)
                    ],
                    key=lambda item: get_number_from_tail(item),
                )

                for file_name in file_names[start_idx:end_idx]:
                    name_list.append(f"{group_name}{sep}{file_name}")

        else:  # for CoSOD
            group_names = os.listdir(data_path)
            group_paths = [os.path.join(data_path, n) for n in group_names]
            for group_path in group_paths:
                group_name = os.path.basename(group_path)

                file_names = sorted(
                    [
                        n[len(name_prefix) : -len(name_suffix)]
                        for n in os.listdir(group_path)
                        if n.startswith(name_prefix) and n.endswith(name_suffix)
                    ],
                    key=lambda item: get_number_from_tail(item),
                )

                for file_name in file_names[start_idx:end_idx]:
                    name_list.append(f"{group_name}{sep}{file_name}")
    name_list = sorted(set(name_list))  # 去重
    return name_list


def get_list_with_suffix(dataset_path: str, suffix: str):
    name_list = []
    if os.path.isfile(dataset_path):
        print(f" ++>> {dataset_path} is a file. <<++ ")
        with open(dataset_path, mode="r", encoding="utf-8") as file:
            line = file.readline()
            while line:
                img_name = os.path.basename(line.split()[0])
                name_list.append(os.path.splitext(img_name)[0])
                line = file.readline()
    else:
        print(f" ++>> {dataset_path} is a folder. <<++ ")
        name_list = [
            os.path.splitext(f)[0] for f in os.listdir(dataset_path) if f.endswith(suffix)
        ]
    name_list = list(set(name_list))
    return name_list


def make_dir(path):
    if not os.path.exists(path):
        print(f"`{path}` does not exist，we will create it.")
        os.makedirs(path)
    else:
        assert os.path.isdir(path), f"`{path}` should be a folder"
        print(f"`{path}`已存在")


def imread_with_checking(path, for_color: bool = True) -> np.ndarray:
    assert os.path.exists(path=path) and os.path.isfile(path=path), path
    if for_color:
        data = cv2.imread(path, flags=cv2.IMREAD_COLOR)
        data = cv2.cvtColor(data, cv2.COLOR_BGR2RGB)
    else:
        data = cv2.imread(path, flags=cv2.IMREAD_GRAYSCALE)
    return data


def get_gt_pre_with_name(
    img_name: str,
    gt_root: str,
    pre_root: str,
    *,
    gt_prefix: str = "",
    pre_prefix: str = "",
    gt_suffix: str = ".png",
    pre_suffix: str = "",
    to_normalize: bool = False,
):
    img_path = os.path.join(pre_root, pre_prefix + img_name + pre_suffix)
    gt_path = os.path.join(gt_root, gt_prefix + img_name + gt_suffix)

    pre = imread_with_checking(img_path, for_color=False)
    gt = imread_with_checking(gt_path, for_color=False)

    if pre.shape != gt.shape:
        pre = cv2.resize(pre, dsize=gt.shape[::-1], interpolation=cv2.INTER_LINEAR).astype(
            np.uint8
        )

    if to_normalize:
        gt = normalize_array(gt, to_binary=True, max_eq_255=True)
        pre = normalize_array(pre, to_binary=False, max_eq_255=True)
    return gt, pre


def get_gt_pre_with_name_and_group(
    img_name: str,
    gt_root: str,
    pre_root: str,
    *,
    gt_prefix: str = "",
    pre_prefix: str = "",
    gt_suffix: str = ".png",
    pre_suffix: str = "",
    to_normalize: bool = False,
    interpolation: int = cv2.INTER_CUBIC,
    sep: str = "<sep>",
):
    group_name, file_name = img_name.split(sep)
    if "*" in gt_root:
        gt_root = gt_root.replace("*", group_name)
    else:
        gt_root = os.path.join(gt_root, group_name)
    if "*" in pre_root:
        pre_root = pre_root.replace("*", group_name)
    else:
        pre_root = os.path.join(pre_root, group_name)
    img_path = os.path.join(pre_root, pre_prefix + file_name + pre_suffix)
    gt_path = os.path.join(gt_root, gt_prefix + file_name + gt_suffix)

    pre = imread_with_checking(img_path, for_color=False)
    gt = imread_with_checking(gt_path, for_color=False)

    if pre.shape != gt.shape:
        pre = cv2.resize(pre, dsize=gt.shape[::-1], interpolation=interpolation).astype(np.uint8)

    if to_normalize:
        gt = normalize_array(gt, to_binary=True, max_eq_255=True)
        pre = normalize_array(pre, to_binary=False, max_eq_255=True)
    return gt, pre


def normalize_array(
    data: np.ndarray, to_binary: bool = False, max_eq_255: bool = True
) -> np.ndarray:
    if max_eq_255:
        data = data / 255
    # else: data is in [0, 1]
    if to_binary:
        data = (data > 0.5).astype(np.uint8)
    else:
        if data.max() != data.min():
            data = (data - data.min()) / (data.max() - data.min())
        data = data.astype(np.float32)
    return data


def get_valid_key_name(data_dict: dict, key_name: str) -> str:
    if data_dict.get(key_name.lower(), "keyerror") == "keyerror":
        key_name = key_name.upper()
    else:
        key_name = key_name.lower()
    return key_name


def get_target_key(target_dict: dict, key: str) -> str:
    """
    from the keys of the target_dict, get the valid key name corresponding to the `key`
    if there is not a valid name, return None
    """
    target_keys = {k.lower(): k for k in target_dict.keys()}
    return target_keys.get(key.lower(), None)


def colored_print(msg: str, mode: str = "general"):
    """
    为不同类型的字符串消息的打印提供一些显示格式的定制

    :param msg: 要输出的字符串消息
    :param mode: 对应的字符串打印模式，目前支持 general/warning/error
    :return:
    """
    if mode == "general":
        msg = msg
    elif mode == "warning":
        msg = f"\033[5;31m{msg}\033[0m"
    elif mode == "error":
        msg = f"\033[1;31m{msg}\033[0m"
    else:
        raise ValueError(f"{mode} is invalid mode.")
    print(msg)


class ColoredPrinter:
    """
    为不同类型的字符串消息的打印提供一些显示格式的定制
    """

    @staticmethod
    def info(msg):
        print(msg)

    @staticmethod
    def warn(msg):
        msg = f"\033[5;31m{msg}\033[0m"
        print(msg)

    @staticmethod
    def error(msg):
        msg = f"\033[1;31m{msg}\033[0m"
        print(msg)


def update_info(source_info: dict, new_info: dict):
    for name, info in source_info.items():
        if name in new_info:
            if isinstance(info, dict):
                update_info(source_info=info, new_info=new_info[name])
            else:  # int, float, list, tuple
                info = new_info[name]
            source_info[name] = info
    return source_info
