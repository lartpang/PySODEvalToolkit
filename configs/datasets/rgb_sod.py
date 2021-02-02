# -*- coding: utf-8 -*-
import os
from collections import OrderedDict

_RGB_SOD_ROOT = "/home/lart/Datasets/Saliency/RGBSOD"

ECSSD = dict(
    root=os.path.join(_RGB_SOD_ROOT, "ECSSD"),
    image=dict(path=os.path.join(_RGB_SOD_ROOT, "ECSSD", "Image"), suffix=".jpg"),
    mask=dict(path=os.path.join(_RGB_SOD_ROOT, "ECSSD", "Mask"), suffix=".png"),
)
DUTOMRON = dict(
    root=os.path.join(_RGB_SOD_ROOT, "DUT-OMRON"),
    image=dict(path=os.path.join(_RGB_SOD_ROOT, "DUT-OMRON", "Image"), suffix=".jpg"),
    mask=dict(path=os.path.join(_RGB_SOD_ROOT, "DUT-OMRON", "Mask"), suffix=".png"),
)
HKUIS = dict(
    root=os.path.join(_RGB_SOD_ROOT, "HKU-IS"),
    image=dict(path=os.path.join(_RGB_SOD_ROOT, "HKU-IS", "Image"), suffix=".png"),
    mask=dict(path=os.path.join(_RGB_SOD_ROOT, "HKU-IS", "Mask"), suffix=".png"),
)
PASCALS = dict(
    root=os.path.join(_RGB_SOD_ROOT, "PASCAL-S"),
    image=dict(path=os.path.join(_RGB_SOD_ROOT, "PASCAL-S", "Image"), suffix=".jpg"),
    mask=dict(path=os.path.join(_RGB_SOD_ROOT, "PASCAL-S", "Mask"), suffix=".png"),
)
SOC_TE = dict(
    root=os.path.join(_RGB_SOD_ROOT, "SOC/Test"),
    image=dict(path=os.path.join(_RGB_SOD_ROOT, "SOC/Test", "Image"), suffix=".jpg"),
    mask=dict(path=os.path.join(_RGB_SOD_ROOT, "SOC/Test", "Mask"), suffix=".png"),
)
DUTS_TE = dict(
    root=os.path.join(_RGB_SOD_ROOT, "DUTS/Test"),
    image=dict(path=os.path.join(_RGB_SOD_ROOT, "DUTS/Test", "Image"), suffix=".jpg"),
    mask=dict(path=os.path.join(_RGB_SOD_ROOT, "DUTS/Test", "Mask"), suffix=".png"),
)
DUTS_TR = dict(
    root=os.path.join(_RGB_SOD_ROOT, "DUTS/Train"),
    image=dict(path=os.path.join(_RGB_SOD_ROOT, "DUTS/Train", "Image"), suffix=".jpg"),
    mask=dict(path=os.path.join(_RGB_SOD_ROOT, "DUTS/Train", "Mask"), suffix=".png"),
)

rgb_sod_data = OrderedDict(
    {
        # "DUTS-TR": DUTS_TR,
        "PASCAL-S": PASCALS,
        "ECSSD": ECSSD,
        "HKU-IS": HKUIS,
        "DUT-OMRON": DUTOMRON,
        "DUTS-TE": DUTS_TE,
        "SOC": SOC_TE,
    }
)
