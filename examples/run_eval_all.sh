#!/usr/bin/env bash

set -euxo pipefail

#$ python eval_all.py --help
#usage: eval_all.py [-h] --dataset-json DATASET_JSON --method-json METHOD_JSON [--metric-npy METRIC_NPY] [--curves-npy CURVES_NPY] [--record-txt RECORD_TXT] [--to-overwrite]
#                   [--record-xlsx RECORD_XLSX] [--include-methods INCLUDE_METHODS [INCLUDE_METHODS ...]] [--exclude-methods EXCLUDE_METHODS [EXCLUDE_METHODS ...]]
#                   [--include-datasets INCLUDE_DATASETS [INCLUDE_DATASETS ...]] [--exclude-datasets EXCLUDE_DATASETS [EXCLUDE_DATASETS ...]] [--num-workers NUM_WORKERS]
#                   [--num-bits NUM_BITS]
#
#Include: Fm Curve/PR Curves/MAE/(max/mean/weighted) Fmeasure/Smeasure/Emeasure
#    NOTE:
#        Our method automatically calculates the intersection of `pre` and `gt`.
#        Currently supported pre naming rules: `prefix + gt_name_wo_ext + suffix_w_ext`
#
#
#optional arguments:
#  -h, --help            show this help message and exit
#  --dataset-json DATASET_JSON
#                        Json file for datasets.
#  --method-json METHOD_JSON
#                        Json file for methods.
#  --metric-npy METRIC_NPY
#                        Npy file for saving metric results.
#  --curves-npy CURVES_NPY
#                        Npy file for saving curve results.
#  --record-txt RECORD_TXT
#                        Txt file for saving metric results.
#  --to-overwrite        To overwrite the txt file.
#  --record-xlsx RECORD_XLSX
#                        Xlsx file for saving metric results.
#  --include-methods INCLUDE_METHODS [INCLUDE_METHODS ...]
#                        Names of only specific methods you want to evaluate.
#  --exclude-methods EXCLUDE_METHODS [EXCLUDE_METHODS ...]
#                        Names of some specific methods you do not want to evaluate.
#  --include-datasets INCLUDE_DATASETS [INCLUDE_DATASETS ...]
#                        Names of only specific datasets you want to evaluate.
#  --exclude-datasets EXCLUDE_DATASETS [EXCLUDE_DATASETS ...]
#                        Names of some specific datasets you do not want to evaluate.
#  --num-workers NUM_WORKERS
#                        Number of workers for multi-threading or multi-processing. Default: 4
#  --num-bits NUM_BITS   Number of decimal places for showing results. Default: 3

python eval_all.py \
    --dataset-json ../configs/datasets/json/rgb_sod.json \
    --method-json ../configs/methods/json/rgb_sod_methods.json \
    --metric-npy ../output/metric.npy \
    --curves-npy ../output/curves.npy \
    --record-txt ../output/rgb_sod.txt \
    --record-xlsx ../output/rgb_sod.xlsx \
    --include-methods MINet_R50_2020 GateNet_2020 \
    --include-datasets ECSSD
