#!/usr/bin/env bash

set -euxo pipefail

#python plot_results.py --help
#usage: plot_results.py [-h] --dataset-json DATASET_JSON --method-json METHOD_JSON --curves-npy CURVES_NPY [--our-method OUR_METHOD] [--num-rows NUM_ROWS]
#                       [--num-col-legend NUM_COL_LEGEND] [--mode {pr,fm}] [--include-methods INCLUDE_METHODS [INCLUDE_METHODS ...]]
#                       [--exclude-methods EXCLUDE_METHODS [EXCLUDE_METHODS ...]] [--include-datasets INCLUDE_DATASETS [INCLUDE_DATASETS ...]]
#                       [--exclude-datasets EXCLUDE_DATASETS [EXCLUDE_DATASETS ...]] [--separated-legend] [--sharey]
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
#  --alias-json ALIAS_JSON
#                        Json file for name aliases of datasets and methods.
#  --curves-npy CURVES_NPY
#                        Npy file for saving curve results.
#  --our-method OUR_METHOD
#                        Name of our method for highlighting it.
#  --num-rows NUM_ROWS   Number of rows for subplots. Default: 1
#  --num-col-legend NUM_COL_LEGEND
#                        Number of columns in the legend. Default: 1
#  --mode {pr,fm}        Mode for plotting. Default: pr
#  --include-methods INCLUDE_METHODS [INCLUDE_METHODS ...]
#                        Names of only specific methods you want to evaluate.
#  --exclude-methods EXCLUDE_METHODS [EXCLUDE_METHODS ...]
#                        Names of some specific methods you do not want to evaluate.
#  --include-datasets INCLUDE_DATASETS [INCLUDE_DATASETS ...]
#                        Names of only specific datasets you want to evaluate.
#  --exclude-datasets EXCLUDE_DATASETS [EXCLUDE_DATASETS ...]
#                        Names of some specific datasets you do not want to evaluate.
#  --separated-legend    Use the separated legend.
#  --sharey              Use the shared y-axis.

python plot_results.py \
    --dataset-json ../configs/datasets/json/rgb_sod.json \
    --method-json ../configs/methods/json/rgb_sod_methods.json \
    --alias-json ./alias_for_plotting.json \
    --curves-npy ../output/curves.npy \
    --num-rows 1 \
    --num-col-legend 2 \
    --mode pr \
    --exclude-datasets SOC \
    --include-methods MINet_R50_2020 GateNet_2020 \
    --separated-legend
