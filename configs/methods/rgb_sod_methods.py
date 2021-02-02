# -*- coding: utf-8 -*-
import os
from collections import OrderedDict

from configs.misc import curve_info_generator, simple_info_generator

_RGBSOD_METHODS_ROOT = "/home/lart/Datasets/Saliency/PaperResults/RGBSOD"
_RGBSOD_DATASET_NAMES = ["PASCAL-S", "ECSSD", "HKU-IS", "DUT-OMRON", "DUTS-TE"]

_METHODS_DIR_NAMES = {
    "DGRL_2018": "DGRL",
    "PAGRN_2018": "PAGRN18",
    "PiCANet_R_2018": "PiCANet-R",
    "RAS_2018": "RAS",
    "AFNet_2019": "AFNet",
    "BASNet_2019": "BASNet",
    "CPD_R_2019": "CPD-R",
    "PoolNet_R_2019": "PoolNet",
    "EGNet_R_2019": "EGNet-R",
    "HRS_D_2019": "HRS-D",
    "ICNet_2019": "ICNet",
    "MLMSNet_2019": "MLMSNet",
    "PAGENet_2019": "PAGE-Net",
    "SCRN_R_2019": "SCRN",
    "F3Net_R_2020": "F3",
    "R3Net_R_2020": "R3Net",
    "GCPANet_2020": "GCPANet_AAAI20",
    "LDF_2020": "LDF_CVPR20",
    "DFI_2020": "DFI_TIP2020",
    "GateNet_2020": "GateNet20",
    "ITSD_2020": "ITSD20",
    "MINet_R_2020": "MINetR20",
}


DGRL_2018 = {
    "PASCAL-S": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _RGBSOD_DATASET_NAMES[0], _METHODS_DIR_NAMES["DGRL_2018"]
        ),
        suffix=".png",
    ),
    "ECSSD": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _RGBSOD_DATASET_NAMES[1], _METHODS_DIR_NAMES["DGRL_2018"]
        ),
        suffix=".png",
    ),
    "HKU-IS": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _RGBSOD_DATASET_NAMES[2], _METHODS_DIR_NAMES["DGRL_2018"]
        ),
        suffix=".png",
    ),
    "DUT-OMRON": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _RGBSOD_DATASET_NAMES[3], _METHODS_DIR_NAMES["DGRL_2018"]
        ),
        suffix=".png",
    ),
    "DUTS-TE": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _RGBSOD_DATASET_NAMES[4], _METHODS_DIR_NAMES["DGRL_2018"]
        ),
        suffix=".png",
    ),
    "SOC": None,
}

PAGRN_2018 = {
    "PASCAL-S": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _RGBSOD_DATASET_NAMES[0], _METHODS_DIR_NAMES["PAGRN_2018"]
        ),
        suffix=".png",
    ),
    "ECSSD": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _RGBSOD_DATASET_NAMES[1], _METHODS_DIR_NAMES["PAGRN_2018"]
        ),
        suffix=".png",
    ),
    "HKU-IS": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _RGBSOD_DATASET_NAMES[2], _METHODS_DIR_NAMES["PAGRN_2018"]
        ),
        suffix=".png",
    ),
    "DUT-OMRON": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _RGBSOD_DATASET_NAMES[3], _METHODS_DIR_NAMES["PAGRN_2018"]
        ),
        suffix=".png",
    ),
    "DUTS-TE": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _RGBSOD_DATASET_NAMES[4], _METHODS_DIR_NAMES["PAGRN_2018"]
        ),
        suffix=".png",
    ),
    "SOC": None,
}

PiCANet_R_2018 = {
    "PASCAL-S": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _RGBSOD_DATASET_NAMES[0], _METHODS_DIR_NAMES["PiCANet_R_2018"]
        ),
        suffix=".png",
    ),
    "ECSSD": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _RGBSOD_DATASET_NAMES[1], _METHODS_DIR_NAMES["PiCANet_R_2018"]
        ),
        suffix=".png",
    ),
    "HKU-IS": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _RGBSOD_DATASET_NAMES[2], _METHODS_DIR_NAMES["PiCANet_R_2018"]
        ),
        suffix=".png",
    ),
    "DUT-OMRON": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _RGBSOD_DATASET_NAMES[3], _METHODS_DIR_NAMES["PiCANet_R_2018"]
        ),
        suffix=".png",
    ),
    "DUTS-TE": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _RGBSOD_DATASET_NAMES[4], _METHODS_DIR_NAMES["PiCANet_R_2018"]
        ),
        suffix=".png",
    ),
    "SOC": None,
}

RAS_2018 = {
    "PASCAL-S": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _RGBSOD_DATASET_NAMES[0], _METHODS_DIR_NAMES["RAS_2018"]
        ),
        suffix=".png",
    ),
    "ECSSD": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _RGBSOD_DATASET_NAMES[1], _METHODS_DIR_NAMES["RAS_2018"]
        ),
        suffix=".png",
    ),
    "HKU-IS": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _RGBSOD_DATASET_NAMES[2], _METHODS_DIR_NAMES["RAS_2018"]
        ),
        suffix=".png",
    ),
    "DUT-OMRON": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _RGBSOD_DATASET_NAMES[3], _METHODS_DIR_NAMES["RAS_2018"]
        ),
        suffix=".png",
    ),
    "DUTS-TE": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _RGBSOD_DATASET_NAMES[4], _METHODS_DIR_NAMES["RAS_2018"]
        ),
        suffix=".png",
    ),
    "SOC": None,
}

AFNet_2019 = {
    "PASCAL-S": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _RGBSOD_DATASET_NAMES[0], _METHODS_DIR_NAMES["AFNet_2019"]
        ),
        suffix=".png",
    ),
    "ECSSD": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _RGBSOD_DATASET_NAMES[1], _METHODS_DIR_NAMES["AFNet_2019"]
        ),
        suffix=".png",
    ),
    "HKU-IS": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _RGBSOD_DATASET_NAMES[2], _METHODS_DIR_NAMES["AFNet_2019"]
        ),
        suffix=".png",
    ),
    "DUT-OMRON": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _RGBSOD_DATASET_NAMES[3], _METHODS_DIR_NAMES["AFNet_2019"]
        ),
        suffix=".png",
    ),
    "DUTS-TE": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _RGBSOD_DATASET_NAMES[4], _METHODS_DIR_NAMES["AFNet_2019"]
        ),
        suffix=".png",
    ),
    "SOC": None,
}

BASNet_2019 = {
    "PASCAL-S": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _RGBSOD_DATASET_NAMES[0], _METHODS_DIR_NAMES["BASNet_2019"]
        ),
        suffix=".png",
    ),
    "ECSSD": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _RGBSOD_DATASET_NAMES[1], _METHODS_DIR_NAMES["BASNet_2019"]
        ),
        suffix=".png",
    ),
    "HKU-IS": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _RGBSOD_DATASET_NAMES[2], _METHODS_DIR_NAMES["BASNet_2019"]
        ),
        suffix=".png",
    ),
    "DUT-OMRON": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _RGBSOD_DATASET_NAMES[3], _METHODS_DIR_NAMES["BASNet_2019"]
        ),
        suffix=".png",
    ),
    "DUTS-TE": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _RGBSOD_DATASET_NAMES[4], _METHODS_DIR_NAMES["BASNet_2019"]
        ),
        suffix=".png",
    ),
    "SOC": None,
}

CPD_R_2019 = {
    "PASCAL-S": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _RGBSOD_DATASET_NAMES[0], _METHODS_DIR_NAMES["CPD_R_2019"]
        ),
        suffix=".png",
    ),
    "ECSSD": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _RGBSOD_DATASET_NAMES[1], _METHODS_DIR_NAMES["CPD_R_2019"]
        ),
        suffix=".png",
    ),
    "HKU-IS": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _RGBSOD_DATASET_NAMES[2], _METHODS_DIR_NAMES["CPD_R_2019"]
        ),
        suffix=".png",
    ),
    "DUT-OMRON": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _RGBSOD_DATASET_NAMES[3], _METHODS_DIR_NAMES["CPD_R_2019"]
        ),
        suffix=".png",
    ),
    "DUTS-TE": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _RGBSOD_DATASET_NAMES[4], _METHODS_DIR_NAMES["CPD_R_2019"]
        ),
        suffix=".png",
    ),
    "SOC": None,
}

PoolNet_R_2019 = {
    "PASCAL-S": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _RGBSOD_DATASET_NAMES[0], _METHODS_DIR_NAMES["PoolNet_R_2019"]
        ),
        suffix=".png",
    ),
    "ECSSD": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _RGBSOD_DATASET_NAMES[1], _METHODS_DIR_NAMES["PoolNet_R_2019"]
        ),
        suffix=".png",
    ),
    "HKU-IS": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _RGBSOD_DATASET_NAMES[2], _METHODS_DIR_NAMES["PoolNet_R_2019"]
        ),
        suffix=".png",
    ),
    "DUT-OMRON": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _RGBSOD_DATASET_NAMES[3], _METHODS_DIR_NAMES["PoolNet_R_2019"]
        ),
        suffix=".png",
    ),
    "DUTS-TE": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _RGBSOD_DATASET_NAMES[4], _METHODS_DIR_NAMES["PoolNet_R_2019"]
        ),
        suffix=".png",
    ),
    "SOC": None,
}

EGNet_R_2019 = {
    "PASCAL-S": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _RGBSOD_DATASET_NAMES[0], _METHODS_DIR_NAMES["EGNet_R_2019"]
        ),
        suffix=".png",
    ),
    "ECSSD": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _RGBSOD_DATASET_NAMES[1], _METHODS_DIR_NAMES["EGNet_R_2019"]
        ),
        suffix=".png",
    ),
    "HKU-IS": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _RGBSOD_DATASET_NAMES[2], _METHODS_DIR_NAMES["EGNet_R_2019"]
        ),
        suffix=".png",
    ),
    "DUT-OMRON": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _RGBSOD_DATASET_NAMES[3], _METHODS_DIR_NAMES["EGNet_R_2019"]
        ),
        suffix=".png",
    ),
    "DUTS-TE": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _RGBSOD_DATASET_NAMES[4], _METHODS_DIR_NAMES["EGNet_R_2019"]
        ),
        suffix=".png",
    ),
    "SOC": None,
}

HRS_D_2019 = {
    "PASCAL-S": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _RGBSOD_DATASET_NAMES[0], _METHODS_DIR_NAMES["HRS_D_2019"]
        ),
        suffix=".png",
    ),
    "ECSSD": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _RGBSOD_DATASET_NAMES[1], _METHODS_DIR_NAMES["HRS_D_2019"]
        ),
        suffix=".png",
    ),
    "HKU-IS": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _RGBSOD_DATASET_NAMES[2], _METHODS_DIR_NAMES["HRS_D_2019"]
        ),
        suffix=".png",
    ),
    "DUT-OMRON": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _RGBSOD_DATASET_NAMES[3], _METHODS_DIR_NAMES["HRS_D_2019"]
        ),
        suffix=".png",
    ),
    "DUTS-TE": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _RGBSOD_DATASET_NAMES[4], _METHODS_DIR_NAMES["HRS_D_2019"]
        ),
        suffix=".png",
    ),
    "SOC": None,
}

ICNet_2019 = {
    "PASCAL-S": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _RGBSOD_DATASET_NAMES[0], _METHODS_DIR_NAMES["ICNet_2019"]
        ),
        suffix=".png",
    ),
    "ECSSD": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _RGBSOD_DATASET_NAMES[1], _METHODS_DIR_NAMES["ICNet_2019"]
        ),
        suffix=".png",
    ),
    "HKU-IS": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _RGBSOD_DATASET_NAMES[2], _METHODS_DIR_NAMES["ICNet_2019"]
        ),
        suffix=".png",
    ),
    "DUT-OMRON": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _RGBSOD_DATASET_NAMES[3], _METHODS_DIR_NAMES["ICNet_2019"]
        ),
        suffix=".png",
    ),
    "DUTS-TE": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _RGBSOD_DATASET_NAMES[4], _METHODS_DIR_NAMES["ICNet_2019"]
        ),
        suffix=".png",
    ),
    "SOC": None,
}

MLMSNet_2019 = {
    "PASCAL-S": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _RGBSOD_DATASET_NAMES[0], _METHODS_DIR_NAMES["MLMSNet_2019"]
        ),
        suffix=".jpg",
    ),
    "ECSSD": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _RGBSOD_DATASET_NAMES[1], _METHODS_DIR_NAMES["MLMSNet_2019"]
        ),
        suffix=".jpg",
    ),
    "HKU-IS": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _RGBSOD_DATASET_NAMES[2], _METHODS_DIR_NAMES["MLMSNet_2019"]
        ),
        suffix=".jpg",
    ),
    "DUT-OMRON": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _RGBSOD_DATASET_NAMES[3], _METHODS_DIR_NAMES["MLMSNet_2019"]
        ),
        suffix=".jpg",
    ),
    "DUTS-TE": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _RGBSOD_DATASET_NAMES[4], _METHODS_DIR_NAMES["MLMSNet_2019"]
        ),
        suffix=".jpg",
    ),
    "SOC": None,
}

PAGENet_2019 = {
    "PASCAL-S": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _RGBSOD_DATASET_NAMES[0], _METHODS_DIR_NAMES["PAGENet_2019"]
        ),
        suffix=".png",
    ),
    "ECSSD": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _RGBSOD_DATASET_NAMES[1], _METHODS_DIR_NAMES["PAGENet_2019"]
        ),
        suffix=".png",
    ),
    "HKU-IS": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _RGBSOD_DATASET_NAMES[2], _METHODS_DIR_NAMES["PAGENet_2019"]
        ),
        suffix=".png",
    ),
    "DUT-OMRON": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _RGBSOD_DATASET_NAMES[3], _METHODS_DIR_NAMES["PAGENet_2019"]
        ),
        suffix=".png",
    ),
    "DUTS-TE": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _RGBSOD_DATASET_NAMES[4], _METHODS_DIR_NAMES["PAGENet_2019"]
        ),
        suffix=".png",
    ),
    "SOC": None,
}

SCRN_R_2019 = {
    "PASCAL-S": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _RGBSOD_DATASET_NAMES[0], _METHODS_DIR_NAMES["SCRN_R_2019"]
        ),
        suffix=".png",
    ),
    "ECSSD": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _RGBSOD_DATASET_NAMES[1], _METHODS_DIR_NAMES["SCRN_R_2019"]
        ),
        suffix=".png",
    ),
    "HKU-IS": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _RGBSOD_DATASET_NAMES[2], _METHODS_DIR_NAMES["SCRN_R_2019"]
        ),
        suffix=".png",
    ),
    "DUT-OMRON": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _RGBSOD_DATASET_NAMES[3], _METHODS_DIR_NAMES["SCRN_R_2019"]
        ),
        suffix=".png",
    ),
    "DUTS-TE": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _RGBSOD_DATASET_NAMES[4], _METHODS_DIR_NAMES["SCRN_R_2019"]
        ),
        suffix=".png",
    ),
    "SOC": None,
}

F3Net_R_2020 = {
    "PASCAL-S": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _RGBSOD_DATASET_NAMES[0], _METHODS_DIR_NAMES["F3Net_R_2020"]
        ),
        suffix=".png",
    ),
    "ECSSD": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _RGBSOD_DATASET_NAMES[1], _METHODS_DIR_NAMES["F3Net_R_2020"]
        ),
        suffix=".png",
    ),
    "HKU-IS": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _RGBSOD_DATASET_NAMES[2], _METHODS_DIR_NAMES["F3Net_R_2020"]
        ),
        suffix=".png",
    ),
    "DUT-OMRON": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _RGBSOD_DATASET_NAMES[3], _METHODS_DIR_NAMES["F3Net_R_2020"]
        ),
        suffix=".png",
    ),
    "DUTS-TE": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _RGBSOD_DATASET_NAMES[4], _METHODS_DIR_NAMES["F3Net_R_2020"]
        ),
        suffix=".png",
    ),
    "SOC": None,
}

R3Net_R_2020 = {
    "PASCAL-S": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _RGBSOD_DATASET_NAMES[0], _METHODS_DIR_NAMES["R3Net_R_2020"]
        ),
        suffix=".png",
    ),
    "ECSSD": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _RGBSOD_DATASET_NAMES[1], _METHODS_DIR_NAMES["R3Net_R_2020"]
        ),
        suffix=".png",
    ),
    "HKU-IS": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _RGBSOD_DATASET_NAMES[2], _METHODS_DIR_NAMES["R3Net_R_2020"]
        ),
        suffix=".png",
    ),
    "DUT-OMRON": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _RGBSOD_DATASET_NAMES[3], _METHODS_DIR_NAMES["R3Net_R_2020"]
        ),
        suffix=".png",
    ),
    "DUTS-TE": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _RGBSOD_DATASET_NAMES[4], _METHODS_DIR_NAMES["R3Net_R_2020"]
        ),
        suffix=".png",
    ),
    "SOC": None,
}

GCPANet_2020 = {
    "PASCAL-S": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _RGBSOD_DATASET_NAMES[0], _METHODS_DIR_NAMES["GCPANet_2020"]
        ),
        suffix=".png",
    ),
    "ECSSD": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _RGBSOD_DATASET_NAMES[1], _METHODS_DIR_NAMES["GCPANet_2020"]
        ),
        suffix=".png",
    ),
    "HKU-IS": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _RGBSOD_DATASET_NAMES[2], _METHODS_DIR_NAMES["GCPANet_2020"]
        ),
        suffix=".png",
    ),
    "DUT-OMRON": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _RGBSOD_DATASET_NAMES[3], _METHODS_DIR_NAMES["GCPANet_2020"]
        ),
        suffix=".png",
    ),
    "DUTS-TE": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _RGBSOD_DATASET_NAMES[4], _METHODS_DIR_NAMES["GCPANet_2020"]
        ),
        suffix=".png",
    ),
    "SOC": None,
}

LDF_2020 = {
    "PASCAL-S": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _RGBSOD_DATASET_NAMES[0], _METHODS_DIR_NAMES["LDF_2020"]
        ),
        suffix=".png",
    ),
    "ECSSD": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _RGBSOD_DATASET_NAMES[1], _METHODS_DIR_NAMES["LDF_2020"]
        ),
        suffix=".png",
    ),
    "HKU-IS": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _RGBSOD_DATASET_NAMES[2], _METHODS_DIR_NAMES["LDF_2020"]
        ),
        suffix=".png",
    ),
    "DUT-OMRON": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _RGBSOD_DATASET_NAMES[3], _METHODS_DIR_NAMES["LDF_2020"]
        ),
        suffix=".png",
    ),
    "DUTS-TE": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _RGBSOD_DATASET_NAMES[4], _METHODS_DIR_NAMES["LDF_2020"]
        ),
        suffix=".png",
    ),
    "SOC": None,
}

DFI_2020 = {
    "PASCAL-S": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _RGBSOD_DATASET_NAMES[0], _METHODS_DIR_NAMES["DFI_2020"]
        ),
        suffix=".png",
    ),
    "ECSSD": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _RGBSOD_DATASET_NAMES[1], _METHODS_DIR_NAMES["DFI_2020"]
        ),
        suffix=".png",
    ),
    "HKU-IS": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _RGBSOD_DATASET_NAMES[2], _METHODS_DIR_NAMES["DFI_2020"]
        ),
        suffix=".png",
    ),
    "DUT-OMRON": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _RGBSOD_DATASET_NAMES[3], _METHODS_DIR_NAMES["DFI_2020"]
        ),
        suffix=".png",
    ),
    "DUTS-TE": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _RGBSOD_DATASET_NAMES[4], _METHODS_DIR_NAMES["DFI_2020"]
        ),
        suffix=".png",
    ),
    "SOC": None,
}

GateNet_2020 = {
    "PASCAL-S": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _RGBSOD_DATASET_NAMES[0], _METHODS_DIR_NAMES["GateNet_2020"]
        ),
        suffix=".png",
    ),
    "ECSSD": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _RGBSOD_DATASET_NAMES[1], _METHODS_DIR_NAMES["GateNet_2020"]
        ),
        suffix=".png",
    ),
    "HKU-IS": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _RGBSOD_DATASET_NAMES[2], _METHODS_DIR_NAMES["GateNet_2020"]
        ),
        suffix=".png",
    ),
    "DUT-OMRON": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _RGBSOD_DATASET_NAMES[3], _METHODS_DIR_NAMES["GateNet_2020"]
        ),
        suffix=".png",
    ),
    "DUTS-TE": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _RGBSOD_DATASET_NAMES[4], _METHODS_DIR_NAMES["GateNet_2020"]
        ),
        suffix=".png",
    ),
    "SOC": None,
}

ITSD_2020 = {
    "PASCAL-S": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _RGBSOD_DATASET_NAMES[0], _METHODS_DIR_NAMES["ITSD_2020"]
        ),
        suffix=".png",
    ),
    "ECSSD": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _RGBSOD_DATASET_NAMES[1], _METHODS_DIR_NAMES["ITSD_2020"]
        ),
        suffix=".png",
    ),
    "HKU-IS": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _RGBSOD_DATASET_NAMES[2], _METHODS_DIR_NAMES["ITSD_2020"]
        ),
        suffix=".png",
    ),
    "DUT-OMRON": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _RGBSOD_DATASET_NAMES[3], _METHODS_DIR_NAMES["ITSD_2020"]
        ),
        suffix=".png",
    ),
    "DUTS-TE": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _RGBSOD_DATASET_NAMES[4], _METHODS_DIR_NAMES["ITSD_2020"]
        ),
        suffix=".png",
    ),
    "SOC": None,
}

MINet_R_2020 = {
    "PASCAL-S": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _RGBSOD_DATASET_NAMES[0], _METHODS_DIR_NAMES["MINet_R_2020"]
        ),
        suffix=".png",
    ),
    "ECSSD": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _RGBSOD_DATASET_NAMES[1], _METHODS_DIR_NAMES["MINet_R_2020"]
        ),
        suffix=".png",
    ),
    "HKU-IS": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _RGBSOD_DATASET_NAMES[2], _METHODS_DIR_NAMES["MINet_R_2020"]
        ),
        suffix=".png",
    ),
    "DUT-OMRON": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _RGBSOD_DATASET_NAMES[3], _METHODS_DIR_NAMES["MINet_R_2020"]
        ),
        suffix=".png",
    ),
    "DUTS-TE": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _RGBSOD_DATASET_NAMES[4], _METHODS_DIR_NAMES["MINet_R_2020"]
        ),
        suffix=".png",
    ),
    "SOC": None,
}

curve_info = curve_info_generator()
methods_info_for_drawing = OrderedDict(
    {
        "DGRL_2018": curve_info(DGRL_2018, "DGRL_2018"),
        "PAGRN_2018": curve_info(PAGRN_2018, "PAGRN_2018"),
        "PiCANet_R_2018": curve_info(PiCANet_R_2018, "PiCANet_R_2018"),
        "RAS_2018": curve_info(RAS_2018, "RAS_2018"),
        "AFNet_2019": curve_info(AFNet_2019, "AFNet_2019"),
        "BASNet_2019": curve_info(BASNet_2019, "BASNet_2019"),
        "CPD_R_2019": curve_info(CPD_R_2019, "CPD_R_2019"),
        "PoolNet_R_2019": curve_info(PoolNet_R_2019, "PoolNet_R_2019"),
        "EGNet_R_2019": curve_info(EGNet_R_2019, "EGNet_R_2019"),
        "HRS_D_2019": curve_info(HRS_D_2019, "HRS_D_2019"),
        "ICNet_2019": curve_info(ICNet_2019, "ICNet_2019"),
        "MLMSNet_2019": curve_info(MLMSNet_2019, "MLMSNet_2019"),
        "PAGENet_2019": curve_info(PAGENet_2019, "PAGENet_2019"),
        "SCRN_R_2019": curve_info(SCRN_R_2019, "SCRN_R_2019"),
        "F3Net_R_2020": curve_info(F3Net_R_2020, "F3Net_R_2020"),
        "R3Net_R_2020": curve_info(R3Net_R_2020, "R3Net_R_2020"),
        "GCPANet_2020": curve_info(GCPANet_2020, "GCPANet_2020"),
        "LDF_2020": curve_info(LDF_2020, "LDF_2020"),
        "DFI_2020": curve_info(DFI_2020, "DFI_2020"),
        "GateNet_2020": curve_info(GateNet_2020, "GateNet_2020"),
        "ITSD_2020": curve_info(ITSD_2020, "ITSD_2020"),
        "MINet_R_2020": curve_info(MINet_R_2020, "MINet_R_2020"),
    }
)
simple_info = simple_info_generator()
methods_info_for_selecting = OrderedDict(
    {
        "DGRL_2018": simple_info(MINet_R_2020, "DGRL_2018"),
        "PAGRN_2018": simple_info(MINet_R_2020, "PAGRN_2018"),
        "PiCANet_R_2018": simple_info(MINet_R_2020, "PiCANet_R_2018"),
        "RAS_2018": simple_info(MINet_R_2020, "RAS_2018"),
        "AFNet_2019": simple_info(MINet_R_2020, "AFNet_2019"),
        "BASNet_2019": simple_info(MINet_R_2020, "BASNet_2019"),
        "CPD_R_2019": simple_info(MINet_R_2020, "CPD_R_2019"),
        "PoolNet_R_2019": simple_info(MINet_R_2020, "PoolNet_R_2019"),
        "EGNet_R_2019": simple_info(MINet_R_2020, "EGNet_R_2019"),
        "HRS_D_2019": simple_info(MINet_R_2020, "HRS_D_2019"),
        "ICNet_2019": simple_info(MINet_R_2020, "ICNet_2019"),
        "MLMSNet_2019": simple_info(MINet_R_2020, "MLMSNet_2019"),
        "PAGENet_2019": simple_info(MINet_R_2020, "PAGENet_2019"),
        "SCRN_R_2019": simple_info(MINet_R_2020, "SCRN_R_2019"),
        "F3Net_R_2020": simple_info(MINet_R_2020, "F3Net_R_2020"),
        "R3Net_R_2020": simple_info(MINet_R_2020, "R3Net_R_2020"),
        "GCPANet_2020": simple_info(MINet_R_2020, "GCPANet_2020"),
        "LDF_2020": simple_info(MINet_R_2020, "LDF_2020"),
        "DFI_2020": simple_info(MINet_R_2020, "DFI_2020"),
        "GateNet_2020": simple_info(MINet_R_2020, "GateNet_2020"),
        "ITSD_2020": simple_info(MINet_R_2020, "ITSD_2020"),
        "MINet_R_2020": simple_info(MINet_R_2020, "MINet_R_2020"),
    }
)
