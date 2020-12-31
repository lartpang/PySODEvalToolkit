# -*- coding: utf-8 -*-
import os
from collections import OrderedDict

from configs.misc import curve_info_generator, simple_info_generator

_COD_METHODS_MAT_ROOT = (
    "/home/lart/Coding/GIT/CODToolbox/Onekey_Evaluation_Code/OnekeyEvaluationCode/Results/Result-COD10K-test"
)
_COD_METHODS_PRED_ROOT = "/home/lart/Datasets/Saliency/PaperResults/COD"
_COD_DATASETS = ["CAMO-mat", "CHAMELEON-mat", "COD10K-mat"]
_COD_METHODS = {
    "FPN": "2017-CVPR-FPN.mat",
    "MaskRCNN": "2017-CVPR-MaskRCNN.mat",
    "PSPNet": "2017-CVPR-PSPNet.mat",
    "UNet++": "2018-DLMIA-UNet++.mat",
    "MSRCNN": "2019-CVPR-MSRCNN.mat",
    "HTC": "2019-CVPR-HTC.mat",
    "PiCANet": "2018-CVPR-PiCANet.mat",
    "BASNet": "2019-CVPR-BASNet.mat",
    "CPD_ResNet": "2019-CVPR-CPD_ResNet.mat",
    "PFANet": "2019-CVPR-PFANet.mat",
    "PoolNet": "2019-CVPR-PoolNet.mat",
    "EGNet": "2019-ICCV-EGNet.mat",
    "F3Net": "F3Net.mat",
    "MINet": "MINet_Res50_COD.mat",
    "GateNet": "GateNet_Res50_COD.mat",
    "ITSD": "ITSD_CVPR2020_COD.mat",
    "ANet_SRM": "2019-CVIU-ANet_SRM.mat",
    "SINet": "2020-CVPR-SINet.mat",
    "Ours": "Ours",
}

# ^(.*?)_mat = \{\n\s{4}('.*?':)(.*?)$\n\s{4}('.*?':)(.*?)$\n\s{4}('.*?':)(.*?)$\n\}
# $1 = {\n\t$2{\n\t\t'path':"",\n\t\t'suffix':"",\n\t\t'mat': $3},\n\t$4{\n\t\t'path':"",\n\t\t'suffix':"",\n\t\t'mat': $5},\n\t$6{\n\t\t'path':"",\n\t\t'suffix':"",\n\t\t'mat': $7}}

FPN = {
    "camo": {
        "path": os.path.join(_COD_METHODS_PRED_ROOT, "2017-CVPR-FPN", "CAMO"),
        "suffix": ".png",
        "mat": os.path.join(_COD_METHODS_MAT_ROOT, _COD_DATASETS[0], _COD_METHODS["FPN"]),
    },
    "chameleon": {
        "path": os.path.join(_COD_METHODS_PRED_ROOT, "2017-CVPR-FPN", "CHAMELEON"),
        "suffix": ".png",
        "mat": os.path.join(_COD_METHODS_MAT_ROOT, _COD_DATASETS[1], _COD_METHODS["FPN"]),
    },
    "cod10k": {
        "path": os.path.join(_COD_METHODS_PRED_ROOT, "2017-CVPR-FPN", "COD10K"),
        "suffix": ".png",
        "mat": os.path.join(_COD_METHODS_MAT_ROOT, _COD_DATASETS[2], _COD_METHODS["FPN"]),
    },
}

MaskRCNN = {
    "camo": {
        "path": os.path.join(_COD_METHODS_PRED_ROOT, "2017-CVPR-MaskRCNN", "CAMO"),
        "suffix": ".png",
        "mat": os.path.join(_COD_METHODS_MAT_ROOT, _COD_DATASETS[0], _COD_METHODS["MaskRCNN"]),
    },
    "chameleon": {
        "path": os.path.join(_COD_METHODS_PRED_ROOT, "2017-CVPR-MaskRCNN", "CHAMELEON"),
        "suffix": ".png",
        "mat": os.path.join(_COD_METHODS_MAT_ROOT, _COD_DATASETS[1], _COD_METHODS["MaskRCNN"]),
    },
    "cod10k": {
        "path": os.path.join(_COD_METHODS_PRED_ROOT, "2017-CVPR-MaskRCNN", "COD10K"),
        "suffix": ".png",
        "mat": os.path.join(_COD_METHODS_MAT_ROOT, _COD_DATASETS[2], _COD_METHODS["MaskRCNN"]),
    },
}

PSPNet = {
    "camo": {
        "path": os.path.join(_COD_METHODS_PRED_ROOT, "2017-CVPR-PSPNet", "CAMO"),
        "suffix": ".png",
        "mat": os.path.join(_COD_METHODS_MAT_ROOT, _COD_DATASETS[0], _COD_METHODS["PSPNet"]),
    },
    "chameleon": {
        "path": os.path.join(_COD_METHODS_PRED_ROOT, "2017-CVPR-PSPNet", "CHAMELEON"),
        "suffix": ".png",
        "mat": os.path.join(_COD_METHODS_MAT_ROOT, _COD_DATASETS[1], _COD_METHODS["PSPNet"]),
    },
    "cod10k": {
        "path": os.path.join(_COD_METHODS_PRED_ROOT, "2017-CVPR-PSPNet", "COD10K"),
        "suffix": ".png",
        "mat": os.path.join(_COD_METHODS_MAT_ROOT, _COD_DATASETS[2], _COD_METHODS["PSPNet"]),
    },
}

PiCANet = {
    "camo": {
        "path": os.path.join(_COD_METHODS_PRED_ROOT, "2018-CVPR-PiCANet", "CAMO"),
        "suffix": ".png",
        "mat": os.path.join(_COD_METHODS_MAT_ROOT, _COD_DATASETS[0], _COD_METHODS["PiCANet"]),
    },
    "chameleon": {
        "path": os.path.join(_COD_METHODS_PRED_ROOT, "2018-CVPR-PiCANet", "CHAMELEON"),
        "suffix": ".png",
        "mat": os.path.join(_COD_METHODS_MAT_ROOT, _COD_DATASETS[1], _COD_METHODS["PiCANet"]),
    },
    "cod10k": {
        "path": os.path.join(_COD_METHODS_PRED_ROOT, "2018-CVPR-PiCANet", "COD10K"),
        "suffix": ".png",
        "mat": os.path.join(_COD_METHODS_MAT_ROOT, _COD_DATASETS[2], _COD_METHODS["PiCANet"]),
    },
}

UNetPP = {
    "camo": {
        "path": os.path.join(_COD_METHODS_PRED_ROOT, "2018-DLMIA-UNet++", "CAMO"),
        "suffix": ".png",
        "mat": os.path.join(_COD_METHODS_MAT_ROOT, _COD_DATASETS[0], _COD_METHODS["UNet++"]),
    },
    "chameleon": {
        "path": os.path.join(_COD_METHODS_PRED_ROOT, "2018-DLMIA-UNet++", "CHAMELEON"),
        "suffix": ".png",
        "mat": os.path.join(_COD_METHODS_MAT_ROOT, _COD_DATASETS[1], _COD_METHODS["UNet++"]),
    },
    "cod10k": {
        "path": os.path.join(_COD_METHODS_PRED_ROOT, "2018-DLMIA-UNet++", "COD10K"),
        "suffix": ".png",
        "mat": os.path.join(_COD_METHODS_MAT_ROOT, _COD_DATASETS[2], _COD_METHODS["UNet++"]),
    },
}

ANet_SRM = {
    "camo": {
        "path": os.path.join(_COD_METHODS_PRED_ROOT, "2019-CVIU-ANet_SRM", "CAMO"),
        "suffix": ".png",
        "mat": os.path.join(_COD_METHODS_MAT_ROOT, _COD_DATASETS[0], _COD_METHODS["ANet_SRM"]),
    },
    "chameleon": None,
    "cod10k": None,
}

BASNet = {
    "camo": {
        "path": os.path.join(_COD_METHODS_PRED_ROOT, "2019-CVPR-BASNet", "CAMO"),
        "suffix": ".png",
        "mat": os.path.join(_COD_METHODS_MAT_ROOT, _COD_DATASETS[0], _COD_METHODS["BASNet"]),
    },
    "chameleon": {
        "path": os.path.join(_COD_METHODS_PRED_ROOT, "2019-CVPR-BASNet", "CHAMELEON"),
        "suffix": ".png",
        "mat": os.path.join(_COD_METHODS_MAT_ROOT, _COD_DATASETS[1], _COD_METHODS["BASNet"]),
    },
    "cod10k": {
        "path": os.path.join(_COD_METHODS_PRED_ROOT, "2019-CVPR-BASNet", "COD10K"),
        "suffix": ".png",
        "mat": os.path.join(_COD_METHODS_MAT_ROOT, _COD_DATASETS[2], _COD_METHODS["BASNet"]),
    },
}

CPD = {
    "camo": {
        "path": os.path.join(_COD_METHODS_PRED_ROOT, "2019-CVPR-CPD_ResNet", "CAMO"),
        "suffix": ".png",
        "mat": os.path.join(_COD_METHODS_MAT_ROOT, _COD_DATASETS[0], _COD_METHODS["CPD_ResNet"]),
    },
    "chameleon": {
        "path": os.path.join(_COD_METHODS_PRED_ROOT, "2019-CVPR-CPD_ResNet", "CHAMELEON"),
        "suffix": ".png",
        "mat": os.path.join(_COD_METHODS_MAT_ROOT, _COD_DATASETS[1], _COD_METHODS["CPD_ResNet"]),
    },
    "cod10k": {
        "path": os.path.join(_COD_METHODS_PRED_ROOT, "2019-CVPR-CPD_ResNet", "COD10K"),
        "suffix": ".png",
        "mat": os.path.join(_COD_METHODS_MAT_ROOT, _COD_DATASETS[2], _COD_METHODS["CPD_ResNet"]),
    },
}

HTC = {
    "camo": {
        "path": os.path.join(_COD_METHODS_PRED_ROOT, "2019-CVPR-HTC", "CAMO"),
        "suffix": ".png",
        "mat": os.path.join(_COD_METHODS_MAT_ROOT, _COD_DATASETS[0], _COD_METHODS["HTC"]),
    },
    "chameleon": {
        "path": os.path.join(_COD_METHODS_PRED_ROOT, "2019-CVPR-HTC", "CHAMELEON"),
        "suffix": ".png",
        "mat": os.path.join(_COD_METHODS_MAT_ROOT, _COD_DATASETS[1], _COD_METHODS["HTC"]),
    },
    "cod10k": {
        "path": os.path.join(_COD_METHODS_PRED_ROOT, "2019-CVPR-HTC", "COD10K"),
        "suffix": ".png",
        "mat": os.path.join(_COD_METHODS_MAT_ROOT, _COD_DATASETS[2], _COD_METHODS["HTC"]),
    },
}

MSRCNN = {
    "camo": {
        "path": os.path.join(_COD_METHODS_PRED_ROOT, "2019-CVPR-MSRCNN", "CAMO"),
        "suffix": ".png",
        "mat": os.path.join(_COD_METHODS_MAT_ROOT, _COD_DATASETS[0], _COD_METHODS["MSRCNN"]),
    },
    "chameleon": {
        "path": os.path.join(_COD_METHODS_PRED_ROOT, "2019-CVPR-MSRCNN", "CHAMELEON"),
        "suffix": ".png",
        "mat": os.path.join(_COD_METHODS_MAT_ROOT, _COD_DATASETS[1], _COD_METHODS["MSRCNN"]),
    },
    "cod10k": {
        "path": os.path.join(_COD_METHODS_PRED_ROOT, "2019-CVPR-MSRCNN", "COD10K"),
        "suffix": ".png",
        "mat": os.path.join(_COD_METHODS_MAT_ROOT, _COD_DATASETS[2], _COD_METHODS["MSRCNN"]),
    },
}

PFANet = {
    "camo": {
        "path": os.path.join(_COD_METHODS_PRED_ROOT, "2019-CVPR-PFANet", "CAMO"),
        "suffix": ".png",
        "mat": os.path.join(_COD_METHODS_MAT_ROOT, _COD_DATASETS[0], _COD_METHODS["PFANet"]),
    },
    "chameleon": {
        "path": os.path.join(_COD_METHODS_PRED_ROOT, "2019-CVPR-PFANet", "CHAMELEON"),
        "suffix": ".png",
        "mat": os.path.join(_COD_METHODS_MAT_ROOT, _COD_DATASETS[1], _COD_METHODS["PFANet"]),
    },
    "cod10k": {
        "path": os.path.join(_COD_METHODS_PRED_ROOT, "2019-CVPR-PFANet", "COD10K"),
        "suffix": ".png",
        "mat": os.path.join(_COD_METHODS_MAT_ROOT, _COD_DATASETS[2], _COD_METHODS["PFANet"]),
    },
}

PoolNet = {
    "camo": {
        "path": os.path.join(_COD_METHODS_PRED_ROOT, "2019-CVPR-PoolNet", "CAMO"),
        "suffix": ".png",
        "mat": os.path.join(_COD_METHODS_MAT_ROOT, _COD_DATASETS[0], _COD_METHODS["PoolNet"]),
    },
    "chameleon": {
        "path": os.path.join(_COD_METHODS_PRED_ROOT, "2019-CVPR-PoolNet", "CHAMELEON"),
        "suffix": ".png",
        "mat": os.path.join(_COD_METHODS_MAT_ROOT, _COD_DATASETS[1], _COD_METHODS["PoolNet"]),
    },
    "cod10k": {
        "path": os.path.join(_COD_METHODS_PRED_ROOT, "2019-CVPR-PoolNet", "COD10K"),
        "suffix": ".png",
        "mat": os.path.join(_COD_METHODS_MAT_ROOT, _COD_DATASETS[2], _COD_METHODS["PoolNet"]),
    },
}

EGNet = {
    "camo": {
        "path": os.path.join(_COD_METHODS_PRED_ROOT, "2019-ICCV-EGNet", "CAMO"),
        "suffix": ".png",
        "mat": os.path.join(_COD_METHODS_MAT_ROOT, _COD_DATASETS[0], _COD_METHODS["EGNet"]),
    },
    "chameleon": {
        "path": os.path.join(_COD_METHODS_PRED_ROOT, "2019-ICCV-EGNet", "CHAMELEON"),
        "suffix": ".png",
        "mat": os.path.join(_COD_METHODS_MAT_ROOT, _COD_DATASETS[1], _COD_METHODS["EGNet"]),
    },
    "cod10k": {
        "path": os.path.join(_COD_METHODS_PRED_ROOT, "2019-ICCV-EGNet", "COD10K"),
        "suffix": ".png",
        "mat": os.path.join(_COD_METHODS_MAT_ROOT, _COD_DATASETS[2], _COD_METHODS["EGNet"]),
    },
}

F3Net = {
    "camo": {
        "path": os.path.join(_COD_METHODS_PRED_ROOT, "F3Net", "CAMO"),
        "suffix": ".png",
        "mat": os.path.join(_COD_METHODS_MAT_ROOT, _COD_DATASETS[0], _COD_METHODS["F3Net"]),
    },
    "chameleon": {
        "path": os.path.join(_COD_METHODS_PRED_ROOT, "F3Net", "CHAMELEON"),
        "suffix": ".png",
        "mat": os.path.join(_COD_METHODS_MAT_ROOT, _COD_DATASETS[1], _COD_METHODS["F3Net"]),
    },
    "cod10k": {
        "path": os.path.join(_COD_METHODS_PRED_ROOT, "F3Net", "COD10K"),
        "suffix": ".png",
        "mat": os.path.join(_COD_METHODS_MAT_ROOT, _COD_DATASETS[2], _COD_METHODS["F3Net"]),
    },
}

MINet = {
    "camo": {
        "path": os.path.join(_COD_METHODS_PRED_ROOT, "MINet_Res50_COD", "camo"),
        "suffix": ".png",
        "mat": os.path.join(_COD_METHODS_MAT_ROOT, _COD_DATASETS[0], _COD_METHODS["MINet"]),
    },
    "chameleon": {
        "path": os.path.join(_COD_METHODS_PRED_ROOT, "MINet_Res50_COD", "chameleon"),
        "suffix": ".png",
        "mat": os.path.join(_COD_METHODS_MAT_ROOT, _COD_DATASETS[1], _COD_METHODS["MINet"]),
    },
    "cod10k": {
        "path": os.path.join(_COD_METHODS_PRED_ROOT, "MINet_Res50_COD", "cod10k"),
        "suffix": ".png",
        "mat": os.path.join(_COD_METHODS_MAT_ROOT, _COD_DATASETS[2], _COD_METHODS["MINet"]),
    },
}

GateNet = {
    "camo": {
        "path": os.path.join(_COD_METHODS_PRED_ROOT, "GateNet_Res50_COD", "CAMO"),
        "suffix": ".png",
        "mat": os.path.join(_COD_METHODS_MAT_ROOT, _COD_DATASETS[0], _COD_METHODS["GateNet"]),
    },
    "chameleon": {
        "path": os.path.join(_COD_METHODS_PRED_ROOT, "GateNet_Res50_COD", "CHAMELEON"),
        "suffix": ".png",
        "mat": os.path.join(_COD_METHODS_MAT_ROOT, _COD_DATASETS[1], _COD_METHODS["GateNet"]),
    },
    "cod10k": {
        "path": os.path.join(_COD_METHODS_PRED_ROOT, "GateNet_Res50_COD", "COD10K"),
        "suffix": ".png",
        "mat": os.path.join(_COD_METHODS_MAT_ROOT, _COD_DATASETS[2], _COD_METHODS["GateNet"]),
    },
}

ITSD = {
    "camo": {
        "path": os.path.join(_COD_METHODS_PRED_ROOT, "ITSD_CVPR2020_COD", "CAMO"),
        "suffix": ".png",
        "mat": os.path.join(_COD_METHODS_MAT_ROOT, _COD_DATASETS[0], _COD_METHODS["ITSD"]),
    },
    "chameleon": {
        "path": os.path.join(_COD_METHODS_PRED_ROOT, "ITSD_CVPR2020_COD", "CHAMELEON"),
        "suffix": ".png",
        "mat": os.path.join(_COD_METHODS_MAT_ROOT, _COD_DATASETS[1], _COD_METHODS["ITSD"]),
    },
    "cod10k": {
        "path": os.path.join(_COD_METHODS_PRED_ROOT, "ITSD_CVPR2020_COD", "COD10K"),
        "suffix": ".png",
        "mat": os.path.join(_COD_METHODS_MAT_ROOT, _COD_DATASETS[2], _COD_METHODS["ITSD"]),
    },
}

SINet = {
    "camo": {
        "path": os.path.join(_COD_METHODS_PRED_ROOT, "2020-CVPR-SINet", "CAMO"),
        "suffix": ".png",
        "mat": os.path.join(_COD_METHODS_MAT_ROOT, _COD_DATASETS[0], _COD_METHODS["SINet"]),
    },
    "chameleon": {
        "path": os.path.join(_COD_METHODS_PRED_ROOT, "2020-CVPR-SINet", "CHAMELEON"),
        "suffix": ".png",
        "mat": os.path.join(_COD_METHODS_MAT_ROOT, _COD_DATASETS[1], _COD_METHODS["SINet"]),
    },
    "cod10k": {
        "path": os.path.join(_COD_METHODS_PRED_ROOT, "2020-CVPR-SINet", "COD10K"),
        "suffix": ".png",
        "mat": os.path.join(_COD_METHODS_MAT_ROOT, _COD_DATASETS[2], _COD_METHODS["SINet"]),
    },
}

Ours = {
    "camo": {
        "path": os.path.join(_COD_METHODS_PRED_ROOT, "Ours", "camo"),
        "suffix": ".png",
        "mat": os.path.join(_COD_METHODS_MAT_ROOT, _COD_DATASETS[0], _COD_METHODS["Ours"]),
    },
    "chameleon": {
        "path": os.path.join(_COD_METHODS_PRED_ROOT, "Ours", "chameleon"),
        "suffix": ".png",
        "mat": os.path.join(_COD_METHODS_MAT_ROOT, _COD_DATASETS[1], _COD_METHODS["Ours"]),
    },
    "cod10k": {
        "path": os.path.join(_COD_METHODS_PRED_ROOT, "Ours", "cod10k"),
        "suffix": ".png",
        "mat": os.path.join(_COD_METHODS_MAT_ROOT, _COD_DATASETS[2], _COD_METHODS["Ours"]),
    },
}

curve_info = curve_info_generator()
methods_info_for_drawing = OrderedDict(
    {
        "FPN": curve_info(FPN, "FPN"),
        "MaskRCNN": curve_info(MaskRCNN, "MaskRCNN"),
        "PSPNet": curve_info(PSPNet, "PSPNet"),
        "UNet++": curve_info(UNetPP, "UNet++"),
        "MSRCNN": curve_info(MSRCNN, "MSRCNN"),
        "HTC": curve_info(HTC, "HTC"),
        "PiCANet": curve_info(PiCANet, "PiCANet"),
        "BASNet": curve_info(BASNet, "BASNet"),
        "CPD": curve_info(CPD, "CPD"),
        "PFANet": curve_info(PFANet, "PFANet"),
        "PoolNet": curve_info(PoolNet, "PoolNet"),
        "EGNet": curve_info(EGNet, "EGNet"),
        "F3Net": curve_info(F3Net, "F3Net"),
        "MINet": curve_info(MINet, "MINet"),
        "ITSD": curve_info(ITSD, "ITSD"),
        "GateNet": curve_info(GateNet, "GateNet"),
        "ANet_SRM": curve_info(ANet_SRM, "ANet_SRM"),
        "SINet": curve_info(SINet, "SINet"),
        "Ours": curve_info(Ours, "Ours", line_color="red", line_width=3),
    }
)

simple_info = simple_info_generator()
methods_info_for_selecting = OrderedDict(
    {
        "FPN": simple_info(FPN, "FPN"),
        "MaskRCNN": simple_info(MaskRCNN, "MaskRCNN"),
        "PSPNet": simple_info(PSPNet, "PSPNet"),
        "UNet++": simple_info(UNetPP, "UNet++"),
        "MSRCNN": simple_info(MSRCNN, "MSRCNN"),
        "HTC": simple_info(HTC, "HTC"),
        "PiCANet": simple_info(PiCANet, "PiCANet"),
        "BASNet": simple_info(BASNet, "BASNet"),
        "CPD": simple_info(CPD, "CPD"),
        "PFANet": simple_info(PFANet, "PFANet"),
        "PoolNet": simple_info(PoolNet, "PoolNet"),
        "EGNet": simple_info(EGNet, "EGNet"),
        "F3Net": simple_info(F3Net, "F3Net"),
        "MINet": simple_info(MINet, "MINet"),
        "ITSD": simple_info(ITSD, "ITSD"),
        "GateNet": simple_info(GateNet, "GateNet"),
        "ANet_SRM": simple_info(ANet_SRM, "ANet_SRM"),
        "SINet": simple_info(SINet, "SINet"),
        "Ours": simple_info(Ours, "Ours"),
    }
)
