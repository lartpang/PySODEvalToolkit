# -*- coding: utf-8 -*-
def print_formatter(
    results: dict, method_name_length=10, metric_name_length=5, metric_value_length=5
):
    dataset_regions = []
    for dataset_name, dataset_metrics in results.items():
        dataset_head_row = f" Dataset: {dataset_name} "
        dataset_region = [dataset_head_row]
        for method_name, metric_info in dataset_metrics.items():
            showed_method_name = clip_string(
                method_name, max_length=method_name_length, mode="left"
            )
            method_row_head = f"{showed_method_name} "
            method_row_body = []
            for metric_name, metric_value in metric_info.items():
                showed_metric_name = clip_string(
                    metric_name, max_length=metric_name_length, mode="right"
                )
                showed_value_string = clip_string(
                    str(metric_value), max_length=metric_value_length, mode="left"
                )
                method_row_body.append(f"{showed_metric_name}: {showed_value_string}")
            method_row = method_row_head + ", ".join(method_row_body)
            dataset_region.append(method_row)
        dataset_region_string = "\n".join(dataset_region)
        dataset_regions.append(dataset_region_string)
    dividing_line = "\n" + "-" * len(dataset_region[-1]) + "\n"  # 直接使用最后一个数据集区域的最后一行数据的长度作为分割线的长度
    formatted_string = dividing_line.join(dataset_regions)
    return formatted_string


def clip_string(string: str, max_length: int, padding_char: str = " ", mode: str = "left"):
    assert isinstance(max_length, int), f"{max_length} must be `int` type"

    real_length = len(string)
    if real_length <= max_length:
        padding_length = max_length - real_length
        if mode == "left":
            clipped_string = string + f"{padding_char}" * padding_length
        elif mode == "middle":
            left_padding_str = f"{padding_char}" * (padding_length // 2)
            right_padding_str = f"{padding_char}" * (padding_length - padding_length // 2)
            clipped_string = left_padding_str + string + right_padding_str
        elif mode == "right":
            clipped_string = f"{padding_char}" * padding_length + string
        else:
            raise NotImplementedError
    else:
        clipped_string = string[:max_length]

    return clipped_string
