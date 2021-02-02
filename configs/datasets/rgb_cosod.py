# -*- coding: utf-8 -*-
import os
from collections import OrderedDict

_RGB_CoSOD_ROOT = "/home/lart/Datasets/Saliency/CoSOD"

COCO9213 = dict(
    root=os.path.join(_RGB_CoSOD_ROOT, "COCO9213"),
    image=dict(path=os.path.join(_RGB_CoSOD_ROOT, "COCO9213-os", "img"), suffix=".png"),
    mask=dict(path=os.path.join(_RGB_CoSOD_ROOT, "COCO9213-os", "gt"), suffix=".png"),
)
CoCA = dict(
    root=os.path.join(_RGB_CoSOD_ROOT, "CoCA"),
    image=dict(path=os.path.join(_RGB_CoSOD_ROOT, "CoCA", "image"), suffix=".jpg"),
    mask=dict(path=os.path.join(_RGB_CoSOD_ROOT, "CoCA", "binary"), suffix=".png"),
    bbox=dict(path=os.path.join(_RGB_CoSOD_ROOT, "CoCA", "bbox"), suffix=".txt"),
    instance=dict(path=os.path.join(_RGB_CoSOD_ROOT, "CoCA", "instance"), suffix=".png"),
)
CoSal2015 = dict(
    root=os.path.join(_RGB_CoSOD_ROOT, "CoSal2015"),
    image=dict(path=os.path.join(_RGB_CoSOD_ROOT, "CoSal2015", "Image"), suffix=".jpg"),
    mask=dict(path=os.path.join(_RGB_CoSOD_ROOT, "CoSal2015", "GroundTruth"), suffix=".png"),
)
CoSOD3k = dict(
    root=os.path.join(_RGB_CoSOD_ROOT, "CoSOD3k"),
    image=dict(path=os.path.join(_RGB_CoSOD_ROOT, "CoSOD3k", "Image"), suffix=".jpg"),
    mask=dict(path=os.path.join(_RGB_CoSOD_ROOT, "CoSOD3k", "GroundTruth"), suffix=".png"),
    bbox=dict(path=os.path.join(_RGB_CoSOD_ROOT, "CoSOD3k", "BoundingBox"), suffix=".txt"),
    instance=dict(
        path=os.path.join(_RGB_CoSOD_ROOT, "CoSOD3k", "SegmentationObject"), suffix=".png"
    ),
)
iCoSeg = dict(
    root=os.path.join(_RGB_CoSOD_ROOT, "iCoSeg"),
    image=dict(path=os.path.join(_RGB_CoSOD_ROOT, "iCoSeg", "Image"), suffix=".jpg"),
    mask=dict(path=os.path.join(_RGB_CoSOD_ROOT, "iCoSeg", "GroundTruth"), suffix=".png"),
)
ImagePair = dict(
    root=os.path.join(_RGB_CoSOD_ROOT, "ImagePair"),
    image=dict(path=os.path.join(_RGB_CoSOD_ROOT, "ImagePair", "Image"), suffix=".jpg"),
    mask=dict(path=os.path.join(_RGB_CoSOD_ROOT, "ImagePair", "GroundTruth"), suffix=".png"),
)
MSRC = dict(
    root=os.path.join(_RGB_CoSOD_ROOT, "MSRC"),
    image=dict(path=os.path.join(_RGB_CoSOD_ROOT, "MSRC", "Image"), suffix=".jpg"),
    mask=dict(path=os.path.join(_RGB_CoSOD_ROOT, "MSRC", "GroundTruth"), suffix=".png"),
)
WICOS = dict(
    root=os.path.join(_RGB_CoSOD_ROOT, "WICOS"),
    image=dict(path=os.path.join(_RGB_CoSOD_ROOT, "WICOS", "Image"), suffix=".jpg"),
    mask=dict(path=os.path.join(_RGB_CoSOD_ROOT, "WICOS", "GroundTruth"), suffix=".png"),
)

# [('ImagePair', 210), ('MSRC', 233), ('WICOS', 364), ('iCoSeg', 643), ('CoCA', 1295), ('CoSal2015', 2015), ('CoSOD3k', 3316)]
rgb_cosod_data = OrderedDict(
    {
        "ImagePair": ImagePair,
        "MSRC": MSRC,
        "WICOS": WICOS,
        "iCoSeg": iCoSeg,
        "CoCA": CoCA,
        "CoSal2015": CoSal2015,
        "CoSOD3k": CoSOD3k,
    }
)
