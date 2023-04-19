# -*- coding: utf-8 -*-

import json
import os
from collections import OrderedDict

from matplotlib import colors

# max = 148
_COLOR_Genarator = iter(
    sorted(
        [
            color
            for name, color in colors.cnames.items()
            if name not in ["red", "white"] or not name.startswith("light") or "gray" in name
        ]
    )
)


def curve_info_generator():
    # TODO 当前尽是对方法依次赋予`-`和`--`，但是对于某一方法仅包含特定数据集的结果时，
    #  会导致确实结果的数据集中的该方法相邻的两个方法style一样
    line_style_flag = True

    def _template_generator(
        method_info: dict, method_name: str, line_color: str = None, line_width: int = 2
    ) -> dict:
        nonlocal line_style_flag
        template_info = dict(
            path_dict=method_info,
            curve_setting=dict(
                line_style="-" if line_style_flag else "--",
                line_label=method_name,
                line_width=line_width,
            ),
        )
        if line_color is not None:
            template_info["curve_setting"]["line_color"] = line_color
        else:
            template_info["curve_setting"]["line_color"] = next(_COLOR_Genarator)

        line_style_flag = not line_style_flag
        return template_info

    return _template_generator


def simple_info_generator():
    def _template_generator(method_info: dict, method_name: str) -> dict:
        template_info = dict(path_dict=method_info, label=method_name)
        return template_info

    return _template_generator


def get_valid_elements(source: list, include_elements: list, exclude_elements: list) -> list:
    targeted_elements = []
    if include_elements and not exclude_elements:  # only include_elements is not [] and not None
        for element in include_elements:
            assert element in source, element
            targeted_elements.append(element)

    elif not include_elements and exclude_elements:  # only exclude_elements is not [] and not None
        for element in exclude_elements:
            assert element in source, element
        for element in source:
            if element not in exclude_elements:
                targeted_elements.append(element)

    elif not include_elements and not exclude_elements:
        targeted_elements = source

    else:
        raise ValueError(
            f"include_elements: {include_elements}\nexclude_elements: {exclude_elements}"
        )

    if not targeted_elements:
        print(source, include_elements, exclude_elements)
        raise ValueError("targeted_elements must be a valid and non-empty list.")
    return targeted_elements


def get_methods_info(
    methods_info_jsons: list,
    include_methods: list,
    exclude_methods: list,
    *,
    for_drawing: bool = False,
    our_name: str = "",
) -> OrderedDict:
    """
    在json文件中存储的对应方法的字典的键值会被直接用于绘图

    :param methods_info_jsons: 保存方法信息的json文件，支持多个文件组合使用，按照输入的顺序依此读取
    :param for_drawing: 是否用于绘制曲线图，True会补充一些绘图信息
    :param our_name: 在绘图时，可以通过指定our_name来使用红色加粗实线强调特定方法的曲线
    :param include_methods: 仅返回列表中指定的方法的信息，为None时，返回所有
    :param exclude_methods: 仅返回列表中指定的方法的信息，为None时，返回所有，与include_datasets必须仅有一个非None
    :return: methods_full_info
    """
    if not isinstance(methods_info_jsons, (list, tuple)):
        methods_info_jsons = [methods_info_jsons]

    methods_info = {}
    for f in methods_info_jsons:
        if not os.path.isfile(f):
            raise FileNotFoundError(f"{f} is not be found!!!")

        with open(f, encoding="utf-8", mode="r") as f:
            methods_info.update(json.load(f, object_hook=OrderedDict))  # 有序载入

    if our_name:
        assert our_name in methods_info, f"{our_name} is not in json file."

    targeted_methods = get_valid_elements(
        source=list(methods_info.keys()),
        include_elements=include_methods,
        exclude_elements=exclude_methods,
    )
    if our_name and our_name in targeted_methods:
        targeted_methods.pop(targeted_methods.index(our_name))
        targeted_methods.insert(0, our_name)

    if for_drawing:
        info_generator = curve_info_generator()
    else:
        info_generator = simple_info_generator()

    methods_full_info = []
    for method_name in targeted_methods:
        method_path = methods_info[method_name]

        if for_drawing and our_name and our_name == method_name:
            method_info = info_generator(method_path, method_name, line_color="red", line_width=3)
        else:
            method_info = info_generator(method_path, method_name)
        methods_full_info.append((method_name, method_info))
    return OrderedDict(methods_full_info)


def get_datasets_info(
    datastes_info_json: str, include_datasets: list, exclude_datasets: list
) -> OrderedDict:
    """
    在json文件中存储的所有数据集的信息会被直接导出到一个字典中

    :param datastes_info_json: 保存方法信息的json文件
    :param include_datasets: 指定读取信息的数据集名字，为None时，读取所有
    :param exclude_datasets: 排除读取信息的数据集名字，为None时，读取所有，与include_datasets必须仅有一个非None
    :return: datastes_full_info
    """

    assert os.path.isfile(datastes_info_json), datastes_info_json
    with open(datastes_info_json, encoding="utf-8", mode="r") as f:
        datasets_info = json.load(f, object_hook=OrderedDict)  # 有序载入

    targeted_datasets = get_valid_elements(
        source=list(datasets_info.keys()),
        include_elements=include_datasets,
        exclude_elements=exclude_datasets,
    )

    datasets_full_info = []
    for dataset_name in targeted_datasets:
        data_path = datasets_info[dataset_name]

        datasets_full_info.append((dataset_name, data_path))
    return OrderedDict(datasets_full_info)
