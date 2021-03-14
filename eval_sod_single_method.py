# -*- coding: utf-8 -*-

import os

from tqdm import tqdm

from utils.generate_info import get_datasets_info
from utils.misc import colored_print, get_gt_pre_with_name, get_name_list, make_dir
from utils.print_formatter import print_formatter
from utils.recorders import MetricExcelRecorder, MetricRecorder

total_info = dict(
    rgb_sod=dict(
        dataset="/home/lart/Coding/Py-SOD-VOS-EvalToolkit/configs/datasets/json/rgb_sod.json",
        method="/home/lart/Coding/Py-SOD-VOS-EvalToolkit/configs/methods/json/rgb_sod_methods.json",
    ),
    rgb_cod=dict(
        dataset="/home/lart/Coding/Py-SOD-VOS-EvalToolkit/configs/datasets/json/rgb_cod.json",
        method="/home/lart/Coding/Py-SOD-VOS-EvalToolkit/configs/methods/json/rgb_cod_methods.json",
    ),
    rgbd_sod=dict(
        dataset="/home/lart/Coding/Py-SOD-VOS-EvalToolkit/configs/datasets/json/rgbd_sod.json",
        method="/home/lart/Coding/Py-SOD-VOS-EvalToolkit/configs/methods/json/rgbd_sod_methods.json",
    ),
)


def cal_all_metrics():
    excel_recorder = MetricExcelRecorder(
        xlsx_path=xlsx_path,
        sheet_name=data_type,
        row_header=["methods"],
        dataset_names=sorted(list(dataset_info.keys())),
        metric_names=["sm", "wfm", "mae", "adpf", "avgf", "maxf", "adpe", "avge", "maxe"],
    )

    metrics = {}
    for dataset_name, dataset_path in dataset_info.items():
        if dataset_name in skipped_names:
            colored_print(msg=f"{dataset_name} will be skipped.", mode="warning")
            continue

        # 获取真值图片信息
        gt_info = dataset_path["mask"]
        gt_root = gt_info["path"]
        gt_ext = gt_info["suffix"]
        # 真值名字列表
        gt_index_file = dataset_path.get("index_file")
        if gt_index_file:
            gt_name_list = get_name_list(data_path=gt_index_file, file_ext=gt_ext)
        else:
            gt_name_list = get_name_list(data_path=gt_root, file_ext=gt_ext)
        assert len(gt_name_list) > 0, "there is not ground truth."

        # ==>> test the intersection between pre and gt for each method <<==
        method_dataset_info = pred_path.get(dataset_name, None)
        if method_dataset_info is None:
            colored_print(
                msg=f"{model_name} does not have results on {dataset_name}", mode="warning"
            )
            continue

        # 预测结果存放路径下的图片文件名字列表和扩展名称
        pre_ext = method_dataset_info["suffix"]
        pre_root = method_dataset_info["path"]
        pre_name_list = get_name_list(data_path=pre_root, file_ext=pre_ext)

        # get the intersection
        eval_name_list = sorted(list(set(gt_name_list).intersection(set(pre_name_list))))
        num_names = len(eval_name_list)

        if num_names == 0:
            colored_print(
                msg=f"{model_name} does not have results on {dataset_name}", mode="warning"
            )
            continue

        colored_print(
            f"Evaluating {model_name} with {len(eval_name_list)} images"
            f" (G:{len(gt_name_list)},P:{len(pre_name_list)}) images on dataset {dataset_name}"
        )

        metric_recoder = MetricRecorder()
        tqdm_bar = tqdm(
            eval_name_list, total=num_names, leave=False, ncols=119, desc=f"({dataset_name})"
        )
        for img_name in tqdm_bar:
            gt, pre = get_gt_pre_with_name(
                gt_root=gt_root,
                pre_root=pre_root,
                img_name=img_name,
                pre_ext=pre_ext,
                gt_ext=gt_ext,
                to_normalize=False,
            )
            metric_recoder.update(pre=pre, gt=gt)
        method_results = metric_recoder.show(num_bits=num_bits, return_ndarray=False)
        method_metrics = method_results["numerical"]
        metrics[dataset_name] = method_metrics

        excel_recorder(row_data=method_metrics, dataset_name=dataset_name, method_name=model_name)

        print(method_metrics)

    formatted_string = print_formatter(metrics)
    colored_print(f"all methods have been tested:\n{formatted_string}")


if __name__ == "__main__":
    data_type = "rgb_sod"
    data_info = total_info[data_type]
    output_path = "./output"  # 存放输出文件的文件夹
    make_dir(output_path)
    model_name = "CoNet"  # 待评估的模型名字
    pred_path = data_info["method"]["selecting"][model_name]  # 待评估的预测结果的路径
    # 包含所有待比较模型结果的信息和绘图配置的字典
    dataset_info = get_datasets_info(datastes_info_json=data_info["dataset"])
    export_xlsx = False  # 是否导出xlsx文件
    xlsx_path = os.path.join(output_path, "resutls.xlsx")  # xlsx文件的路径
    num_bits = 3  # 评估结果保留的小数点后数据的位数
    skipped_names = []  # 可以跳过指定的数据集
    cal_all_metrics()
