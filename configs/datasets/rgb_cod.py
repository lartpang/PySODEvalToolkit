# -*- coding: utf-8 -*-
import os
from collections import OrderedDict

_RGB_COD_ROOT = "/home/lart/Datasets/Saliency/COD"

chameleon_path = dict(
    root=os.path.join(_RGB_COD_ROOT, "Test", "CHAMELEON"),
    image=dict(path=os.path.join(_RGB_COD_ROOT, "Test", "CHAMELEON", "Image"), suffix=".jpg"),
    mask=dict(path=os.path.join(_RGB_COD_ROOT, "Test", "CHAMELEON", "Mask"), suffix=".png"),
)
camo_path = dict(
    root=os.path.join(_RGB_COD_ROOT, "Test", "CAMO"),
    image=dict(path=os.path.join(_RGB_COD_ROOT, "Test", "CAMO", "Image"), suffix=".jpg"),
    mask=dict(path=os.path.join(_RGB_COD_ROOT, "Test", "CAMO", "Mask"), suffix=".png"),
)
cod10k_path = dict(
    root=os.path.join(_RGB_COD_ROOT, "Test", "COD10K"),
    image=dict(path=os.path.join(_RGB_COD_ROOT, "Test", "COD10K", "Image"), suffix=".jpg"),
    mask=dict(path=os.path.join(_RGB_COD_ROOT, "Test", "COD10K", "Mask"), suffix=".png"),
)

rgb_cod_data = OrderedDict({"CHAMELEON": chameleon_path, "CAMO": camo_path, "COD10K": cod10k_path})
