# -*- coding: utf-8 -*-
import os
from collections import OrderedDict

from configs.utils.config_generator import curve_info_generator, simple_info_generator

_CoSOD_METHODS_ROOT = "/home/lart/Datasets/Saliency/PaperResults/CoSOD"
ICNet = {
    "CoCA": dict(
        path=os.path.join(_CoSOD_METHODS_ROOT, "NIPS2020_ICNet_os", "CoCA"), suffix=".png"
    ),
    "CoSal2015": dict(
        path=os.path.join(_CoSOD_METHODS_ROOT, "NIPS2020_ICNet_os", "CoSal2015"), suffix=".png"
    ),
    "CoSOD3k": dict(
        path=os.path.join(_CoSOD_METHODS_ROOT, "NIPS2020_ICNet_os", "CoSOD3k"), suffix=".png"
    ),
    "iCoSeg": dict(
        path=os.path.join(_CoSOD_METHODS_ROOT, "NIPS2020_ICNet_os", "iCoSeg"), suffix=".png"
    ),
    "ImagePair": None,
    "MSRC": dict(
        path=os.path.join(_CoSOD_METHODS_ROOT, "NIPS2020_ICNet_os", "MSRC"), suffix=".png"
    ),
    "WICOS": None,
}

_Ours_ROOT = "/home/lart/Coding/CoCODProj/output"
_Ours_FPN_ROOT = os.path.join(_Ours_ROOT, "Ours")
Ours_FPN = {
    "CoCA": dict(path=os.path.join(_Ours_FPN_ROOT, "pre/coca"), suffix=".png"),
    "CoSal2015": dict(path=os.path.join(_Ours_FPN_ROOT, "pre/cosal2015"), suffix=".png"),
    "CoSOD3k": dict(path=os.path.join(_Ours_FPN_ROOT, "pre/cosod3k"), suffix=".png"),
    "iCoSeg": dict(path=os.path.join(_Ours_FPN_ROOT, "pre/icoseg"), suffix=".png"),
    "ImagePair": dict(path=os.path.join(_Ours_FPN_ROOT, "pre/imagepair"), suffix=".png"),
    "MSRC": dict(path=os.path.join(_Ours_FPN_ROOT, "pre/msrc"), suffix=".png"),
    "WICOS": dict(path=os.path.join(_Ours_FPN_ROOT, "pre/wicos"), suffix=".png"),
}

curve_info = curve_info_generator()
methods_info_for_drawing = OrderedDict(
    {
        "ICNet": curve_info(ICNet, "ICNet"),
        "Ours_FPN": curve_info(Ours_FPN, "Ours_FPN"),
    }
)
simple_info = simple_info_generator()
methods_info_for_selecting = OrderedDict(
    {
        "ICNet": simple_info(ICNet, "ICNet"),
        "Ours_FPN": simple_info(Ours_FPN, "Ours_FPN"),
    }
)
