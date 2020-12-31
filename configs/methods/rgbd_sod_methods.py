# -*- coding: utf-8 -*-
import os
from collections import OrderedDict

from configs.misc import curve_info_generator, simple_info_generator

# \s{4}"(.*?)": (os.*?),$
# "$1": dict(path=$2, suffix='.png'),
HDFNet_VGG16_root = "/home/lart/Coding/HDFFile/output/HDFNet/HDFNet_VGG16"
HDFNet_VGG16 = {
    "LFSD": dict(path=os.path.join(HDFNet_VGG16_root, "lfsd"), suffix=".png"),
    "NJUD": dict(path=os.path.join(HDFNet_VGG16_root, "njud"), suffix=".png"),
    "NLPR": dict(path=os.path.join(HDFNet_VGG16_root, "nlpr"), suffix=".png"),
    "RGBD135": dict(path=os.path.join(HDFNet_VGG16_root, "rgbd135"), suffix=".png"),
    "SIP": dict(path=os.path.join(HDFNet_VGG16_root, "sip"), suffix=".png"),
    "SSD": dict(path=os.path.join(HDFNet_VGG16_root, "ssd"), suffix=".png"),
    "STEREO797": dict(path=os.path.join(HDFNet_VGG16_root, "stereo797"), suffix=".png"),
    "STEREO1000": dict(path=os.path.join(HDFNet_VGG16_root, "stereo1000"), suffix=".png"),
    "DUTRGBD": dict(path=os.path.join(HDFNet_VGG16_root, "dutrgbd"), suffix=".png"),
}

HDFNet_VGG19_root = "/home/lart/Coding/HDFFile/output/HDFNet/HDFNet_VGG19"
HDFNet_VGG19 = {
    "LFSD": dict(path=os.path.join(HDFNet_VGG19_root, "lfsd"), suffix=".png"),
    "NJUD": dict(path=os.path.join(HDFNet_VGG19_root, "njud"), suffix=".png"),
    "NLPR": dict(path=os.path.join(HDFNet_VGG19_root, "nlpr"), suffix=".png"),
    "RGBD135": dict(path=os.path.join(HDFNet_VGG19_root, "rgbd135"), suffix=".png"),
    "SIP": dict(path=os.path.join(HDFNet_VGG19_root, "sip"), suffix=".png"),
    "SSD": dict(path=os.path.join(HDFNet_VGG19_root, "ssd"), suffix=".png"),
    "STEREO797": dict(path=os.path.join(HDFNet_VGG19_root, "stereo797"), suffix=".png"),
    "STEREO1000": dict(path=os.path.join(HDFNet_VGG19_root, "stereo1000"), suffix=".png"),
    "DUTRGBD": dict(path=os.path.join(HDFNet_VGG19_root, "dutrgbd"), suffix=".png"),
}

HDFNet_Res50_root = "/home/lart/Coding/HDFFile/output/HDFNet/HDFNet_Res50"
HDFNet_Res50 = {
    "LFSD": dict(path=os.path.join(HDFNet_Res50_root, "lfsd"), suffix=".png"),
    "NJUD": dict(path=os.path.join(HDFNet_Res50_root, "njud"), suffix=".png"),
    "NLPR": dict(path=os.path.join(HDFNet_Res50_root, "nlpr"), suffix=".png"),
    "RGBD135": dict(path=os.path.join(HDFNet_Res50_root, "rgbd135"), suffix=".png"),
    "SIP": dict(path=os.path.join(HDFNet_Res50_root, "sip"), suffix=".png"),
    "SSD": dict(path=os.path.join(HDFNet_Res50_root, "ssd"), suffix=".png"),
    "STEREO797": dict(path=os.path.join(HDFNet_Res50_root, "stereo797"), suffix=".png"),
    "STEREO1000": dict(path=os.path.join(HDFNet_Res50_root, "stereo1000"), suffix=".png"),
    "DUTRGBD": dict(path=os.path.join(HDFNet_Res50_root, "dutrgbd"), suffix=".png"),
}

UCNet_root = "/home/lart/Datasets/Saliency/PaperResults/RGBDSOD/CVPR2020_UCNet"
UCNet = {
    "LFSD": dict(path=os.path.join(UCNet_root, "LFSD"), suffix=".png"),
    "NJUD": dict(path=os.path.join(UCNet_root, "NJU2K"), suffix=".png"),
    "NLPR": dict(path=os.path.join(UCNet_root, "NLPR"), suffix=".png"),
    "RGBD135": dict(path=os.path.join(UCNet_root, "DES"), suffix=".png"),
    "SIP": dict(path=os.path.join(UCNet_root, "SIP"), suffix=".png"),
    "SSD": None,
    "STEREO797": None,
    "STEREO1000": dict(path=os.path.join(UCNet_root, "STERE"), suffix=".png"),
    "DUTRGBD": None,
}

JLDCF_root = "/home/lart/Datasets/Saliency/PaperResults/RGBDSOD/CVPR2020_JL-DCF"
JLDCF = {
    "LFSD": dict(path=os.path.join(JLDCF_root, "LFSD"), suffix=".png"),
    "NJUD": dict(path=os.path.join(JLDCF_root, "NJU2K"), suffix=".png"),
    "NLPR": dict(path=os.path.join(JLDCF_root, "NLPR"), suffix=".png"),
    "RGBD135": dict(path=os.path.join(JLDCF_root, "RGBD135"), suffix=".png"),
    "SIP": dict(path=os.path.join(JLDCF_root, "SIP"), suffix=".png"),
    "SSD": None,
    "STEREO797": None,
    "STEREO1000": dict(path=os.path.join(JLDCF_root, "STERE"), suffix=".png"),
    "DUTRGBD": dict(path=os.path.join(JLDCF_root, "DUT-RGBD-testing"), suffix=".png"),
}

S2MA_root = "/home/lart/Datasets/Saliency/PaperResults/RGBDSOD/CVPR2020_S2MA"
S2MA = {
    "LFSD": dict(path=os.path.join(S2MA_root, "LFSD"), suffix=".png"),
    "NJUD": dict(path=os.path.join(S2MA_root, "NJU2K"), suffix=".png"),
    "NLPR": dict(path=os.path.join(S2MA_root, "NLPR"), suffix=".png"),
    "RGBD135": dict(path=os.path.join(S2MA_root, "RGBD135"), suffix=".png"),
    "SIP": None,
    "SSD": dict(path=os.path.join(S2MA_root, "SSD100"), suffix=".png"),
    "STEREO797": None,
    "STEREO1000": dict(path=os.path.join(S2MA_root, "STERE"), suffix=".png"),
    "DUTRGBD": dict(path=os.path.join(S2MA_root, "DUT-RGBD"), suffix=".png"),
}

CoNet_root = "/home/lart/Datasets/Saliency/PaperResults/RGBDSOD/ECCV2020_CoNet"
CoNet = {
    "LFSD": dict(path=os.path.join(CoNet_root, "LFSD"), suffix=".png"),
    "NJUD": dict(path=os.path.join(CoNet_root, "NJUD"), suffix=".png"),
    "NLPR": dict(path=os.path.join(CoNet_root, "NLPR"), suffix=".png"),
    "RGBD135": dict(path=os.path.join(CoNet_root, "RGBD135"), suffix=".png"),
    "SIP": dict(path=os.path.join(CoNet_root, "SIP"), suffix=".png"),
    "SSD": dict(path=os.path.join(CoNet_root, "SSD"), suffix=".png"),
    "STEREO797": dict(path=os.path.join(CoNet_root, "STEREO"), suffix=".png"),
    "STEREO1000": None,
    "DUTRGBD": dict(path=os.path.join(CoNet_root, "DUT-RGBD"), suffix=".png"),
}

BBSNet_root = "/home/lart/Datasets/Saliency/PaperResults/RGBDSOD/ECCV2020_BBSNet"
BBSNet = {
    "LFSD": dict(path=os.path.join(BBSNet_root, "LFSD"), suffix=".png"),
    "NJUD": dict(path=os.path.join(BBSNet_root, "NJU2K"), suffix=".png"),
    "NLPR": dict(path=os.path.join(BBSNet_root, "NLPR"), suffix=".png"),
    "RGBD135": dict(path=os.path.join(BBSNet_root, "DES"), suffix=".png"),
    "SIP": dict(path=os.path.join(BBSNet_root, "SIP"), suffix=".png"),
    "SSD": dict(path=os.path.join(BBSNet_root, "SSD"), suffix=".png"),
    "STEREO797": None,
    "STEREO1000": dict(path=os.path.join(BBSNet_root, "STERE"), suffix=".png"),
    "DUTRGBD": dict(path=os.path.join(BBSNet_root, "DUT"), suffix=".png"),
}

CMWNet_root = "/home/lart/Datasets/Saliency/PaperResults/RGBDSOD/ECCV2020_CMWNet"
CMWNet = {
    "LFSD": dict(path=os.path.join(CMWNet_root, "LFSD"), suffix=".png"),
    "NJUD": dict(path=os.path.join(CMWNet_root, "NJU2K"), suffix=".png"),
    "NLPR": dict(path=os.path.join(CMWNet_root, "NLPR"), suffix=".png"),
    "RGBD135": dict(path=os.path.join(CMWNet_root, "DES"), suffix=".png"),
    "SIP": dict(path=os.path.join(CMWNet_root, "SIP"), suffix=".png"),
    "SSD": dict(path=os.path.join(CMWNet_root, "SSD"), suffix=".png"),
    "STEREO797": None,
    "STEREO1000": dict(path=os.path.join(CMWNet_root, "STEREO"), suffix=".png"),
    "DUTRGBD": dict(path=os.path.join(CMWNet_root, "DUT-RGBD"), suffix=".png"),
}

curve_info = curve_info_generator()
methods_info_for_drawing = OrderedDict(
    {
        "HDFNet_VGG16": curve_info(HDFNet_VGG16, "HDFNet_VGG16"),
        "HDFNet_VGG19": curve_info(HDFNet_VGG19, "HDFNet_VGG19"),
        "HDFNet_Res50": curve_info(HDFNet_Res50, "HDFNet_Res50"),
        "UCNet": curve_info(UCNet, "UCNet"),
        "JLDCF": curve_info(JLDCF, "JLDCF"),
        "S2MA": curve_info(S2MA, "S2MA"),
        "CoNet": curve_info(CoNet, "CoNet"),
        "BBSNet": curve_info(BBSNet, "BBSNet"),
        "CMWNet": curve_info(CMWNet, "CMWNet"),
    }
)

simple_info = simple_info_generator()
methods_info_for_selecting = OrderedDict(
    {
        "HDFNet_VGG16": simple_info(HDFNet_VGG16, "HDFNet_VGG16"),
        "HDFNet_VGG19": simple_info(HDFNet_VGG19, "HDFNet_VGG19"),
        "HDFNet_Res50": simple_info(HDFNet_Res50, "HDFNet_Res50"),
        "UCNet": simple_info(UCNet, "UCNet"),
        "JLDCF": simple_info(JLDCF, "JLDCF"),
        "S2MA": simple_info(S2MA, "S2MA"),
        "CoNet": simple_info(CoNet, "CoNet"),
        "BBSNet": simple_info(BBSNet, "BBSNet"),
        "CMWNet": simple_info(CMWNet, "CMWNet"),
    }
)
