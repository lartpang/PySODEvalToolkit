# -*- coding: utf-8 -*-
import copy
import os
from pprint import pprint

from tqdm import tqdm

from configs import total_info
from configs.methods import rgbd_sod_methods
from utils.misc import get_gt_pre_with_name, get_name_list, make_dir
from utils.recorders import MetricExcelRecorder, MetricRecorder


def cal_all_metrics():
    excel_recorder = MetricExcelRecorder(
        xlsx_path=xlsx_path,
        sheet_name=data_type,
        row_header=["methods"],
        dataset_names=sorted(list(dataset_info.keys())),
        metric_names=["sm", "wfm", "mae", "adpf", "avgf", "maxf", "adpe", "avge", "maxe"],
    )

    method_perf = {}
    for dataset_name, dataset_path in dataset_info.items():
        if dataset_name in skipped_names:
            print(f" ++>> {dataset_name} will be skipped.")
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
            print(f" ==>> {model_name} does not have results on {dataset_name} <<== ")
            continue

        # 预测结果存放路径下的图片文件名字列表和扩展名称
        pre_ext = method_dataset_info["suffix"]
        pre_root = method_dataset_info["path"]
        pre_name_list = get_name_list(data_path=pre_root, file_ext=pre_ext)

        # get the intersection
        eval_name_list = sorted(list(set(gt_name_list).intersection(set(pre_name_list))))
        print(
            f" ==>> It is evaluating {model_name} with {len(eval_name_list)} images"
            f" (G:{len(gt_name_list)},P:{len(pre_name_list)}) images on dataset {dataset_name} <<== "
        )

        metric_recoder = MetricRecorder()
        tqdm_bar = tqdm(
            eval_name_list,
            total=len(eval_name_list),
            leave=False,
            ncols=119,
            desc=f"({dataset_name})",
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
        metric_results = metric_recoder.show(bit_num=None)  # 保留原始数据

        perf_on_dataset = copy.deepcopy(metric_results)
        del perf_on_dataset["fm"]
        del perf_on_dataset["em"]
        del perf_on_dataset["p"]
        del perf_on_dataset["r"]

        perf_on_dataset["meanFm"] = metric_results["fm"].mean()
        perf_on_dataset["maxFm"] = metric_results["fm"].max()
        perf_on_dataset["meanEm"] = metric_results["em"].mean()
        perf_on_dataset["maxEm"] = metric_results["em"].max()
        perf_on_dataset = {k: v.round(bit_num) for k, v in perf_on_dataset.items()}
        print(perf_on_dataset)
        method_perf[dataset_name] = perf_on_dataset
    excel_recorder(
        row_data=method_perf[dataset_name],
        dataset_name=dataset_name,
        method_name=model_name,
    )
    pprint(method_perf)


if __name__ == "__main__":
    data_type = "rgb_sod"
    data_info = total_info[data_type]
    output_path = "./output"  # 存放输出文件的文件夹
    make_dir(output_path)

    pred_path = rgbd_sod_methods.CoNet  # 待评估的预测结果的路径
    model_name = "CoNet"  # 待评估的模型名字
    dataset_info = data_info["dataset"]
    export_xlsx = False  # 是否导出xlsx文件
    xlsx_path = os.path.join(output_path, "resutls.xlsx")  # xlsx文件的路径
    bit_num = 3  # 评估结果保留的小数点后数据的位数
    skipped_names = []  # 可以跳过指定的数据集
    cal_all_metrics()
