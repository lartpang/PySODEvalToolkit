# -*- coding: utf-8 -*-
import os

import cv2
import numpy as np
from PIL import Image


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


def get_name_list(data_path: str, file_ext: str = None) -> tuple:
    if os.path.isfile(data_path):
        assert data_path.endswith((".txt", ".lst"))
        data_list = []
        with open(data_path, encoding="utf-8", mode="r") as f:
            line = f.readline().strip()
            while line:
                data_list.append(line)
                line = f.readline().strip()
        file_ext = None  # 使用name list时不需要指定ext了
    else:
        data_list = os.listdir(data_path)

    if file_ext is not None:
        name_list = [os.path.splitext(f)[0] for f in data_list if f.endswith(file_ext)]
    else:
        name_list = [os.path.splitext(f)[0] for f in data_list]

    name_list = list(set(name_list))
    return name_list


def get_name_with_group_list(data_path: str, file_ext: str = None) -> list:
    name_list = []
    if os.path.isfile(data_path):
        print(f" ++>> {data_path} is a file. <<++ ")
        with open(data_path, mode="r", encoding="utf-8") as file:
            line = file.readline()
            while line:
                img_name_with_group = line.split()
                name_list.append(os.path.splitext(img_name_with_group)[0])
                line = file.readline()
    else:
        print(f" ++>> {data_path} is a folder. <<++ ")
        group_names = sorted(os.listdir(data_path))
        for group_name in group_names:
            image_names = [
                "/".join([group_name, x])
                for x in sorted(os.listdir(os.path.join(data_path, group_name)))
            ]
            if file_ext is not None:
                name_list += [os.path.splitext(f)[0] for f in image_names if f.endswith(file_ext)]
            else:
                name_list += [os.path.splitext(f)[0] for f in image_names]
    # group_name/file_name.ext
    name_list = list(set(name_list))  # 去重
    return name_list


def get_list_with_postfix(dataset_path: str, postfix: str):
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
            os.path.splitext(f)[0] for f in os.listdir(dataset_path) if f.endswith(postfix)
        ]
    name_list = list(set(name_list))
    return name_list


def rgb_loader(path):
    with open(path, "rb") as f:
        img = Image.open(f)
        return img.convert("L")


def binary_loader(path):
    assert os.path.exists(path), f"`{path}` does not exist."
    with open(path, "rb") as f:
        img = Image.open(f)
        return img.convert("L")


def load_data(pre_root, gt_root, name, postfixs):
    pre = binary_loader(os.path.join(pre_root, name + postfixs[0]))
    gt = binary_loader(os.path.join(gt_root, name + postfixs[1]))
    return pre, gt


def normalize_pil(pre, gt):
    gt = np.asarray(gt)
    pre = np.asarray(pre)
    gt = gt / (gt.max() + 1e-8)
    gt = np.where(gt > 0.5, 1, 0)
    max_pre = pre.max()
    min_pre = pre.min()
    if max_pre == min_pre:
        pre = pre / 255
    else:
        pre = (pre - min_pre) / (max_pre - min_pre)
    return pre, gt


def make_dir(path):
    if not os.path.exists(path):
        print(f"`{path}` does not exist，we will create it.")
        os.makedirs(path)
    else:
        assert os.path.isdir(path), f"`{path}` should be a folder"
        print(f"`{path}`已存在")


def imread_wich_checking(path, for_color: bool = True, with_cv2: bool = True) -> np.ndarray:
    assert os.path.exists(path=path) and os.path.isfile(path=path), path
    if with_cv2:
        if for_color:
            data = cv2.imread(path, flags=cv2.IMREAD_COLOR)
            data = cv2.cvtColor(data, cv2.COLOR_BGR2RGB)
        else:
            data = cv2.imread(path, flags=cv2.IMREAD_GRAYSCALE)
    else:
        data = np.array(Image.open(path).convert("RGB" if for_color else "L"))
    return data


def get_gt_pre_with_name(
    gt_root: str,
    pre_root: str,
    img_name: str,
    pre_ext: str,
    gt_ext: str = ".png",
    to_normalize: bool = False,
):
    img_path = os.path.join(pre_root, img_name + pre_ext)
    gt_path = os.path.join(gt_root, img_name + gt_ext)

    pre = imread_wich_checking(img_path, for_color=False)
    gt = imread_wich_checking(gt_path, for_color=False)

    if pre.shape != gt.shape:
        pre = cv2.resize(pre, dsize=gt.shape[::-1], interpolation=cv2.INTER_LINEAR).astype(
            np.uint8
        )

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
