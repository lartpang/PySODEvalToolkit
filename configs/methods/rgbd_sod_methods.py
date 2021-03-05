# -*- coding: utf-8 -*-
import os
from collections import OrderedDict

from configs.utils.config_generator import curve_info_generator, simple_info_generator

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

CoNet_root = "/home/lart/Datasets/Saliency/PaperResults/RGBDSOD/2020-ECCV-CoNet"
CoNet = {
    "LFSD": dict(path=os.path.join(CoNet_root, "LFSD"), suffix=".png"),
    "NJUD": dict(path=os.path.join(CoNet_root, "NJUD"), suffix=".png"),
    "NLPR": dict(path=os.path.join(CoNet_root, "NLPR"), suffix=".png"),
    "RGBD135": dict(path=os.path.join(CoNet_root, "RGBD135"), suffix=".png"),
    "SIP": dict(path=os.path.join(CoNet_root, "SIP"), suffix=".png"),
    "SSD": dict(path=os.path.join(CoNet_root, "SSD"), suffix=".png"),
    "STEREO797": dict(path=os.path.join(CoNet_root, "STEREO"), suffix=".png"),
    "STEREO1000": dict(path=os.path.join(CoNet_root, "STERE1000"), suffix=".png"),
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

FRDT_root = "/home/lart/Datasets/Saliency/PaperResults/RGBDSOD/2020-ACMMM-FRDT"
FRDT = {
    "LFSD": dict(path=os.path.join(FRDT_root, "LFSD"), suffix=".png"),
    "NJUD": dict(path=os.path.join(FRDT_root, "NJUD"), suffix=".png"),
    "NLPR": dict(path=os.path.join(FRDT_root, "NLPR"), suffix=".png"),
    "RGBD135": dict(path=os.path.join(FRDT_root, "RGBD-135"), suffix=".png"),
    "SIP": None,
    "SSD": dict(path=os.path.join(FRDT_root, "SSD"), suffix=".png"),
    "STEREO797": dict(path=os.path.join(FRDT_root, "STEREO"), suffix=".png"),
    "STEREO1000": None,
    "DUTRGBD": dict(path=os.path.join(FRDT_root, "DUT"), suffix=".png"),
}

S2MA_root = "/home/lart/Datasets/Saliency/PaperResults/RGBDSOD/2020-CVPR-S2MA"
S2MA = {
    "LFSD": dict(path=os.path.join(S2MA_root, "LFSD"), suffix=".png"),
    "NJUD": dict(path=os.path.join(S2MA_root, "NJU2K"), suffix=".png"),
    "NLPR": dict(path=os.path.join(S2MA_root, "NLPR"), suffix=".png"),
    "RGBD135": dict(path=os.path.join(S2MA_root, "RGBD135"), suffix=".png"),
    "SIP": dict(path=os.path.join(S2MA_root, "SIP"), suffix=".png"),
    "SSD": dict(path=os.path.join(S2MA_root, "SSD100"), suffix=".png"),
    "STEREO797": None,
    "STEREO1000": dict(path=os.path.join(S2MA_root, "STERE"), suffix=".png"),
    "DUTRGBD": dict(path=os.path.join(S2MA_root, "DUT-RGBD"), suffix=".png"),
}

UCNet_root = (
    "/home/lart/Datasets/Saliency/PaperResults/RGBDSOD/2020-CVPR-UCNet_Res50/CVPR-UCNet_R50"
)
UCNet = {
    "LFSD": dict(path=os.path.join(UCNet_root, "LFSD"), suffix=".png"),
    "NJUD": dict(path=os.path.join(UCNet_root, "NJU2K"), suffix=".png"),
    "NLPR": dict(path=os.path.join(UCNet_root, "NLPR"), suffix=".png"),
    "RGBD135": dict(path=os.path.join(UCNet_root, "DES"), suffix=".png"),
    "SIP": dict(path=os.path.join(UCNet_root, "SIP"), suffix=".png"),
    "SSD": None,
    "STEREO797": None,
    "STEREO1000": dict(path=os.path.join(UCNet_root, "STERE"), suffix=".png"),
    "DUTRGBD": dict(path=os.path.join(UCNet_root, "DUT"), suffix=".png"),
}

UCNet_ABP_root = (
    "/home/lart/Datasets/Saliency/PaperResults/RGBDSOD/2020-CVPR-UCNet_Res50/TPAMI_UCNet_R50_ABP"
)
UCNet_ABP = {
    "LFSD": dict(path=os.path.join(UCNet_ABP_root, "LFSD"), suffix=".png"),
    "NJUD": dict(path=os.path.join(UCNet_ABP_root, "NJU2K"), suffix=".png"),
    "NLPR": dict(path=os.path.join(UCNet_ABP_root, "NLPR"), suffix=".png"),
    "RGBD135": dict(path=os.path.join(UCNet_ABP_root, "DES"), suffix=".png"),
    "SIP": dict(path=os.path.join(UCNet_ABP_root, "SIP"), suffix=".png"),
    "SSD": None,
    "STEREO797": None,
    "STEREO1000": dict(path=os.path.join(UCNet_ABP_root, "STERE"), suffix=".png"),
    "DUTRGBD": None,
}

UCNet_CVAE_root = (
    "/home/lart/Datasets/Saliency/PaperResults/RGBDSOD/2020-CVPR-UCNet_Res50/TPAMI_UCNet_R50_CVAE"
)
UCNet_CVAE = {
    "LFSD": dict(path=os.path.join(UCNet_CVAE_root, "LFSD"), suffix=".png"),
    "NJUD": dict(path=os.path.join(UCNet_CVAE_root, "NJU2K"), suffix=".png"),
    "NLPR": dict(path=os.path.join(UCNet_CVAE_root, "NLPR"), suffix=".png"),
    "RGBD135": dict(path=os.path.join(UCNet_CVAE_root, "DES"), suffix=".png"),
    "SIP": dict(path=os.path.join(UCNet_CVAE_root, "SIP"), suffix=".png"),
    "SSD": None,
    "STEREO797": None,
    "STEREO1000": dict(path=os.path.join(UCNet_CVAE_root, "STERE"), suffix=".png"),
    "DUTRGBD": None,
}

CasGNN_root = "/home/lart/Datasets/Saliency/PaperResults/RGBDSOD/2020-ECCV-CasGNN"
CasGNN = {
    "LFSD": dict(path=os.path.join(CasGNN_root, "LFSD", "pred"), suffix=".png"),
    "NJUD": dict(path=os.path.join(CasGNN_root, "NJUD", "pred"), suffix=".png"),
    "NLPR": dict(path=os.path.join(CasGNN_root, "NLPR", "pred"), suffix=".png"),
    "RGBD135": dict(path=os.path.join(CasGNN_root, "DES", "pred"), suffix=".png"),
    "SIP": None,
    "SSD": dict(path=os.path.join(CasGNN_root, "SSD", "pred"), suffix=".png"),
    "STEREO797": None,
    "STEREO1000": dict(path=os.path.join(CasGNN_root, "STERE", "pred"), suffix=".png"),
    "DUTRGBD": dict(path=os.path.join(CasGNN_root, "DUT-RGBD", "pred"), suffix=".png"),
}

DANet_VGG16_root = (
    "/home/lart/Datasets/Saliency/PaperResults/RGBDSOD/2020-ECCV-DANet_VGG/DANet_vgg16"
)
DANet_VGG16 = {
    "LFSD": dict(path=os.path.join(DANet_VGG16_root, "LFSD"), suffix=".png"),
    "NJUD": dict(path=os.path.join(DANet_VGG16_root, "NJUD"), suffix=".png"),
    "NLPR": dict(path=os.path.join(DANet_VGG16_root, "NLPR"), suffix=".png"),
    "RGBD135": dict(path=os.path.join(DANet_VGG16_root, "RGBD135"), suffix=".png"),
    "SIP": dict(path=os.path.join(DANet_VGG16_root, "SIP"), suffix=".png"),
    "SSD": dict(path=os.path.join(DANet_VGG16_root, "SSD"), suffix=".png"),
    "STEREO797": None,
    "STEREO1000": dict(path=os.path.join(DANet_VGG16_root, "STERE"), suffix=".png"),
    "DUTRGBD": dict(path=os.path.join(DANet_VGG16_root, "DUT-RGBD"), suffix=".png"),
}

DANet_VGG19_root = (
    "/home/lart/Datasets/Saliency/PaperResults/RGBDSOD/2020-ECCV-DANet_VGG/DANet_vgg19"
)
DANet_VGG19 = {
    "LFSD": dict(path=os.path.join(DANet_VGG19_root, "LFSD"), suffix=".png"),
    "NJUD": dict(path=os.path.join(DANet_VGG19_root, "NJUD"), suffix=".png"),
    "NLPR": dict(path=os.path.join(DANet_VGG19_root, "NLPR"), suffix=".png"),
    "RGBD135": dict(path=os.path.join(DANet_VGG19_root, "RGBD135"), suffix=".png"),
    "SIP": dict(path=os.path.join(DANet_VGG19_root, "SIP"), suffix=".png"),
    "SSD": dict(path=os.path.join(DANet_VGG19_root, "SSD"), suffix=".png"),
    "STEREO797": None,
    "STEREO1000": dict(path=os.path.join(DANet_VGG19_root, "STERE"), suffix=".png"),
    "DUTRGBD": dict(path=os.path.join(DANet_VGG19_root, "DUT-RGBD"), suffix=".png"),
}

PGAR_root = "/home/lart/Datasets/Saliency/PaperResults/RGBDSOD/2020-ECCV-PGAR"
PGAR = {
    "LFSD": dict(path=os.path.join(PGAR_root, "LFSD"), suffix=".png"),
    "NJUD": dict(path=os.path.join(PGAR_root, "NJUD_test"), suffix=".png"),
    "NLPR": dict(path=os.path.join(PGAR_root, "NLPR_test"), suffix=".png"),
    "RGBD135": dict(path=os.path.join(PGAR_root, "RGBD135"), suffix=".png"),
    "SIP": dict(path=os.path.join(PGAR_root, "SIP"), suffix=".png"),
    "SSD": None,
    "STEREO797": None,
    "STEREO1000": dict(path=os.path.join(PGAR_root, "STERE"), suffix=".png"),
    "DUTRGBD": dict(path=os.path.join(PGAR_root, "DUT-RGBD"), suffix=".png"),
}

DisenFuse_root = "/home/lart/Datasets/Saliency/PaperResults/RGBDSOD/2020-TIP-DisenFuse_VGG16"
DisenFuse = {
    "LFSD": dict(path=os.path.join(DisenFuse_root, "LFSD"), suffix=".png"),
    "NJUD": dict(path=os.path.join(DisenFuse_root, "NJUD"), suffix=".png"),
    "NLPR": dict(path=os.path.join(DisenFuse_root, "NLPR"), suffix=".jpg"),
    "RGBD135": dict(path=os.path.join(DisenFuse_root, "DES"), suffix=".bmp"),
    "SIP": dict(path=os.path.join(DisenFuse_root, "SIP"), suffix=".png"),
    "SSD": None,
    "STEREO797": None,
    "STEREO1000": dict(path=os.path.join(DisenFuse_root, "STEREO1000"), suffix=".png"),
    "DUTRGBD": dict(path=os.path.join(DisenFuse_root, "DUT"), suffix=".png"),
}

DPANet_root = "/home/lart/Datasets/Saliency/PaperResults/RGBDSOD/2020-TIP-DPANet"
DPANet = {
    "LFSD": dict(path=os.path.join(DPANet_root, "LFSD"), suffix=".png"),
    "NJUD": dict(path=os.path.join(DPANet_root, "NJUD"), suffix=".png"),
    "NLPR": dict(path=os.path.join(DPANet_root, "NLPR"), suffix=".png"),
    "RGBD135": dict(path=os.path.join(DPANet_root, "RGBD135"), suffix=".png"),
    "SIP": dict(path=os.path.join(DPANet_root, "SIP"), suffix=".png"),
    "SSD": dict(path=os.path.join(DPANet_root, "SSD100"), suffix=".png"),
    "STEREO797": dict(path=os.path.join(DPANet_root, "STEREO797"), suffix=".png"),
    "STEREO1000": None,
    "DUTRGBD": dict(path=os.path.join(DPANet_root, "DUT"), suffix=".png"),
}

ICNet_root = "/home/lart/Datasets/Saliency/PaperResults/RGBDSOD/2020-TIP-ICNet"
ICNet = {
    "LFSD": dict(path=os.path.join(ICNet_root, "LFSD"), suffix=".png"),
    "NJUD": dict(path=os.path.join(ICNet_root, "NJU2K"), suffix=".png"),
    "NLPR": dict(path=os.path.join(ICNet_root, "NLPR"), suffix=".png"),
    "RGBD135": dict(path=os.path.join(ICNet_root, "DES"), suffix=".png"),
    "SIP": dict(path=os.path.join(ICNet_root, "SIP"), suffix=".png"),
    "SSD": dict(path=os.path.join(ICNet_root, "SSD"), suffix=".png"),
    "STEREO797": None,
    "STEREO1000": dict(path=os.path.join(ICNet_root, "STERE"), suffix=".png"),
    "DUTRGBD": dict(path=os.path.join(ICNet_root, "DUT-RGBD"), suffix=".png"),
}

D3Net_root = "/home/lart/Datasets/Saliency/PaperResults/RGBDSOD/2020-TNNLS-D3Net"
D3Net = {
    "LFSD": dict(path=os.path.join(D3Net_root, "LFSD"), suffix=".png"),
    "NJUD": dict(path=os.path.join(D3Net_root, "NJU2K_TEST"), suffix=".png"),
    "NLPR": dict(path=os.path.join(D3Net_root, "NLPR_TEST"), suffix=".png"),
    "RGBD135": dict(path=os.path.join(D3Net_root, "DES"), suffix=".png"),
    "SIP": dict(path=os.path.join(D3Net_root, "SIP"), suffix=".png"),
    "SSD": dict(path=os.path.join(D3Net_root, "SSD"), suffix=".png"),
    "STEREO797": None,
    "STEREO1000": dict(path=os.path.join(D3Net_root, "STERE"), suffix=".png"),
    "DUTRGBD": dict(path=os.path.join(D3Net_root, "DUT-RGBD_TEST"), suffix=".png"),
}

RD3D_root = "/home/lart/Datasets/Saliency/PaperResults/RGBDSOD/2021-AAAI-RD3D"
RD3D = {
    "LFSD": dict(path=os.path.join(RD3D_root, "LFSD"), suffix=".png"),
    "NJUD": dict(path=os.path.join(RD3D_root, "NJU2000"), suffix=".png"),
    "NLPR": dict(path=os.path.join(RD3D_root, "NLPR"), suffix=".png"),
    "RGBD135": dict(path=os.path.join(RD3D_root, "RGBD135"), suffix=".png"),
    "SIP": dict(path=os.path.join(RD3D_root, "SIP"), suffix=".png"),
    "SSD": None,
    "STEREO797": None,
    "STEREO1000": dict(path=os.path.join(RD3D_root, "STERE"), suffix=".png"),
    "DUTRGBD": dict(path=os.path.join(RD3D_root, "DUT"), suffix=".png"),
}

AFNet_root = "/home/lart/Datasets/Saliency/PaperResults/RGBDSOD/AFNet"
AFNet = {
    "LFSD": dict(path=os.path.join(AFNet_root, "LFSD"), suffix=".png"),
    "NJUD": dict(path=os.path.join(AFNet_root, "NJU2K-TEST"), suffix=".png"),
    "NLPR": dict(path=os.path.join(AFNet_root, "NLPR-TEST"), suffix=".png"),
    "RGBD135": dict(path=os.path.join(AFNet_root, "DES"), suffix=".png"),
    "SIP": dict(path=os.path.join(AFNet_root, "SIP"), suffix=".png"),
    "SSD": dict(path=os.path.join(AFNet_root, "SSD"), suffix=".png"),
    "STEREO797": dict(path=os.path.join(AFNet_root, "STEREO"), suffix=".png"),
    "STEREO1000": dict(path=os.path.join(AFNet_root, "STERE"), suffix=".png"),
    "DUTRGBD": None,
}

CDCP_root = "/home/lart/Datasets/Saliency/PaperResults/RGBDSOD/CDCP"
CDCP = {
    "LFSD": dict(path=os.path.join(CDCP_root, "LFSD"), suffix=".png"),
    "NJUD": dict(path=os.path.join(CDCP_root, "NJUD"), suffix=".png"),
    "NLPR": dict(path=os.path.join(CDCP_root, "NLPR"), suffix=".png"),
    "RGBD135": dict(path=os.path.join(CDCP_root, "RGBD135"), suffix=".png"),
    "SIP": dict(path=os.path.join(CDCP_root, "SIP"), suffix=".png"),
    "SSD": dict(path=os.path.join(CDCP_root, "SSD"), suffix=".png"),
    "STEREO797": None,
    "STEREO1000": dict(path=os.path.join(CDCP_root, "STERE"), suffix=".png"),
    "DUTRGBD": dict(path=os.path.join(CDCP_root, "DUT-RGBD"), suffix=".png"),
}

CPFP_root = "/home/lart/Datasets/Saliency/PaperResults/RGBDSOD/CPFP"
CPFP = {
    "LFSD": dict(path=os.path.join(CPFP_root, "LFSD"), suffix=".png"),
    "NJUD": dict(path=os.path.join(CPFP_root, "NJUD"), suffix=".png"),
    "NLPR": dict(path=os.path.join(CPFP_root, "NLPR"), suffix=".png"),
    "RGBD135": dict(path=os.path.join(CPFP_root, "RGBD135"), suffix=".png"),
    "SIP": dict(path=os.path.join(CPFP_root, "SIP"), suffix=".png"),
    "SSD": dict(path=os.path.join(CPFP_root, "SSD"), suffix=".png"),
    "STEREO797": None,
    "STEREO1000": dict(path=os.path.join(CPFP_root, "STERE"), suffix=".png"),
    "DUTRGBD": dict(path=os.path.join(CPFP_root, "DUT-RGBD"), suffix=".png"),
}

CTMF_root = "/home/lart/Datasets/Saliency/PaperResults/RGBDSOD/CTMF"
CTMF = {
    "LFSD": dict(path=os.path.join(CTMF_root, "LFSD"), suffix=".png"),
    "NJUD": dict(path=os.path.join(CTMF_root, "NJUD"), suffix=".png"),
    "NLPR": dict(path=os.path.join(CTMF_root, "NLPR"), suffix=".jpg"),
    "RGBD135": dict(path=os.path.join(CTMF_root, "RGBD135"), suffix=".bmp"),
    "SIP": dict(path=os.path.join(CTMF_root, "SIP"), suffix=".png"),
    "SSD": dict(path=os.path.join(CTMF_root, "SSD"), suffix=".png"),
    "STEREO797": None,
    "STEREO1000": dict(path=os.path.join(CTMF_root, "STERE"), suffix=".png"),
    "DUTRGBD": dict(path=os.path.join(CTMF_root, "DUT-RGBD"), suffix=".png"),
}

DCMC_root = "/home/lart/Datasets/Saliency/PaperResults/RGBDSOD/DCMC"
DCMC = {
    "LFSD": dict(path=os.path.join(DCMC_root, "LFSD"), suffix=".png"),
    "NJUD": dict(path=os.path.join(DCMC_root, "NJUD"), suffix=".png"),
    "NLPR": dict(path=os.path.join(DCMC_root, "NLPR"), suffix=".png"),
    "RGBD135": dict(path=os.path.join(DCMC_root, "RGBD135"), suffix=".png"),
    "SIP": dict(path=os.path.join(DCMC_root, "SIP"), suffix=".png"),
    "SSD": dict(path=os.path.join(DCMC_root, "SSD"), suffix=".png"),
    "STEREO797": dict(path=os.path.join(DCMC_root, "STEREO"), suffix=".png"),
    "STEREO1000": dict(path=os.path.join(DCMC_root, "STERE"), suffix=".png"),
    "DUTRGBD": dict(path=os.path.join(DCMC_root, "DUT-RGBD"), suffix=".png"),
}

DES_root = "/home/lart/Datasets/Saliency/PaperResults/RGBDSOD/DES"
DES = {
    "LFSD": dict(path=os.path.join(DES_root, "LFSD"), suffix=".png"),
    "NJUD": dict(path=os.path.join(DES_root, "NJUD"), suffix=".png"),
    "NLPR": dict(path=os.path.join(DES_root, "NLPR"), suffix=".png"),
    "RGBD135": dict(path=os.path.join(DES_root, "RGBD135"), suffix=".png"),
    "SIP": dict(path=os.path.join(DES_root, "SIP"), suffix=".png"),
    "SSD": dict(path=os.path.join(DES_root, "SSD"), suffix=".png"),
    "STEREO797": dict(path=os.path.join(DES_root, "STEREO"), suffix=".png"),
    "STEREO1000": dict(path=os.path.join(DES_root, "STERE"), suffix=".png"),
    "DUTRGBD": dict(path=os.path.join(DES_root, "DUT-RGBD"), suffix=".png"),
}

DF_root = "/home/lart/Datasets/Saliency/PaperResults/RGBDSOD/DF"
DF = {
    "LFSD": dict(path=os.path.join(DF_root, "LFSD"), suffix=".png"),
    "NJUD": dict(path=os.path.join(DF_root, "NJUD"), suffix=".png"),
    "NLPR": dict(path=os.path.join(DF_root, "NLPR"), suffix=".png"),
    "RGBD135": dict(path=os.path.join(DF_root, "RGBD135"), suffix=".png"),
    "SIP": dict(path=os.path.join(DF_root, "SIP/SIP"), suffix=".png"),
    "SSD": dict(path=os.path.join(DF_root, "SSD"), suffix=".png"),
    "STEREO797": dict(path=os.path.join(DF_root, "STEREO"), suffix=".png"),
    "STEREO1000": dict(path=os.path.join(DF_root, "STERE"), suffix=".png"),
    "DUTRGBD": dict(path=os.path.join(DF_root, "DUT-RGBD"), suffix=".png"),
}

DMRA_root = "/home/lart/Datasets/Saliency/PaperResults/RGBDSOD/DMRA"
DMRA = {
    "LFSD": dict(path=os.path.join(DMRA_root, "LFSD"), suffix=".png"),
    "NJUD": dict(path=os.path.join(DMRA_root, "NJUD"), suffix=".png"),
    "NLPR": dict(path=os.path.join(DMRA_root, "NLPR"), suffix=".png"),
    "RGBD135": dict(path=os.path.join(DMRA_root, "RGBD135"), suffix=".png"),
    "SIP": dict(path=os.path.join(DMRA_root, "SIP_FromAuthor"), suffix=".png"),
    "SSD": dict(path=os.path.join(DMRA_root, "SSD"), suffix=".png"),
    "STEREO797": dict(path=os.path.join(DMRA_root, "STEREO"), suffix=".png"),
    "STEREO1000": dict(path=os.path.join(DMRA_root, "STERE"), suffix=".png"),
    "DUTRGBD": dict(path=os.path.join(DMRA_root, "DUT-RGBD"), suffix=".png"),
}

MB_root = "/home/lart/Datasets/Saliency/PaperResults/RGBDSOD/MB"
MB = {
    "LFSD": dict(path=os.path.join(MB_root, "LFSD"), suffix=".png"),
    "NJUD": dict(path=os.path.join(MB_root, "NJUD"), suffix=".png"),
    "NLPR": dict(path=os.path.join(MB_root, "NLPR"), suffix=".png"),
    "RGBD135": dict(path=os.path.join(MB_root, "RGBD135"), suffix=".png"),
    "SIP": None,
    "SSD": dict(path=os.path.join(MB_root, "SSD"), suffix=".png"),
    "STEREO797": dict(path=os.path.join(MB_root, "STEREO"), suffix=".png"),
    "STEREO1000": None,
    "DUTRGBD": dict(path=os.path.join(MB_root, "DUT-RGBD"), suffix=".png"),
}

MMCI_root = "/home/lart/Datasets/Saliency/PaperResults/RGBDSOD/MMCI"
MMCI = {
    "LFSD": dict(path=os.path.join(MMCI_root, "LFSD"), suffix=".png"),
    "NJUD": dict(path=os.path.join(MMCI_root, "NJUD"), suffix=".png"),
    "NLPR": dict(path=os.path.join(MMCI_root, "NLPR"), suffix=".jpg"),
    "RGBD135": dict(path=os.path.join(MMCI_root, "RGBD135"), suffix=".bmp"),
    "SIP": dict(path=os.path.join(MMCI_root, "SIP"), suffix=".png"),
    "SSD": dict(path=os.path.join(MMCI_root, "SSD"), suffix=".png"),
    "STEREO797": dict(path=os.path.join(MMCI_root, "STEREO"), suffix=".png"),
    "STEREO1000": dict(path=os.path.join(MMCI_root, "STERE"), suffix=".png"),
    "DUTRGBD": dict(path=os.path.join(MMCI_root, "DUT-RGBD"), suffix=".png"),
}

NLPR_root = "/home/lart/Datasets/Saliency/PaperResults/RGBDSOD/NLPR"
NLPR = {
    "LFSD": dict(path=os.path.join(NLPR_root, "LFSD"), suffix=".png"),
    "NJUD": dict(path=os.path.join(NLPR_root, "NJUD"), suffix=".png"),
    "NLPR": dict(path=os.path.join(NLPR_root, "NLPR"), suffix=".png"),
    "RGBD135": dict(path=os.path.join(NLPR_root, "RGBD135"), suffix=".png"),
    "SIP": dict(path=os.path.join(NLPR_root, "SIP"), suffix=".png"),
    "SSD": dict(path=os.path.join(NLPR_root, "SSD"), suffix=".png"),
    "STEREO797": dict(path=os.path.join(NLPR_root, "STEREO-797"), suffix=".png"),
    "STEREO1000": dict(path=os.path.join(NLPR_root, "STERE"), suffix=".png"),
    "DUTRGBD": dict(path=os.path.join(NLPR_root, "DUT-RGBD"), suffix=".png"),
}

PCANet_root = "/home/lart/Datasets/Saliency/PaperResults/RGBDSOD/PCANet"
PCANet = {
    "LFSD": dict(path=os.path.join(PCANet_root, "LFSD"), suffix=".png"),
    "NJUD": dict(path=os.path.join(PCANet_root, "NJUD"), suffix=".png"),
    "NLPR": dict(path=os.path.join(PCANet_root, "NLPR"), suffix=".jpg"),
    "RGBD135": dict(path=os.path.join(PCANet_root, "RGBD135"), suffix=".png"),
    "SIP": dict(path=os.path.join(PCANet_root, "SIP"), suffix=".png"),
    "SSD": dict(path=os.path.join(PCANet_root, "SSD"), suffix=".png"),
    "STEREO797": dict(path=os.path.join(PCANet_root, "STEREO"), suffix=".png"),
    "STEREO1000": dict(path=os.path.join(PCANet_root, "STERE"), suffix=".png"),
    "DUTRGBD": dict(path=os.path.join(PCANet_root, "DUT-RGBD"), suffix=".png"),
}

# 当前数据有问题暂时不测
PDNet_root = "/home/lart/Datasets/Saliency/PaperResults/RGBDSOD/PDNet"
PDNet = {
    "LFSD": dict(path=os.path.join(PDNet_root, "LFSD"), suffix=".png"),
    "NJUD": dict(path=os.path.join(PDNet_root, "NJUD"), suffix=".png"),
    "NLPR": dict(path=os.path.join(PDNet_root, "NLPR"), suffix=".png"),
    "RGBD135": dict(path=os.path.join(PDNet_root, "RGBD135"), suffix=".png"),
    "SIP": None,
    "SSD": dict(path=os.path.join(PDNet_root, "SSD"), suffix=".png"),
    "STEREO797": dict(path=os.path.join(PDNet_root, "STEREO"), suffix=".png"),
    "STEREO1000": None,
    "DUTRGBD": dict(path=os.path.join(PDNet_root, "DUT-RGBD"), suffix=".png"),
}

TANet_root = "/home/lart/Datasets/Saliency/PaperResults/RGBDSOD/TANet"
TANet = {
    "LFSD": dict(path=os.path.join(TANet_root, "LFSD"), suffix=".png"),
    "NJUD": dict(path=os.path.join(TANet_root, "NJUD"), suffix=".png"),
    "NLPR": dict(path=os.path.join(TANet_root, "NLPR"), suffix=".png"),
    "RGBD135": dict(path=os.path.join(TANet_root, "RGBD135"), suffix=".png"),
    "SIP": dict(path=os.path.join(TANet_root, "SIP"), suffix=".png"),
    "SSD": dict(path=os.path.join(TANet_root, "SSD"), suffix=".png"),
    "STEREO797": dict(path=os.path.join(TANet_root, "STEREO"), suffix=".png"),
    "STEREO1000": dict(path=os.path.join(TANet_root, "STERE"), suffix=".png"),
    "DUTRGBD": dict(path=os.path.join(TANet_root, "DUT-RGBD"), suffix=".png"),
}

curve_info = curve_info_generator()
methods_info_for_drawing = OrderedDict(
    {
        "HDFNet_VGG16": curve_info(HDFNet_VGG16, "HDFNet_VGG16"),
        "HDFNet_VGG19": curve_info(HDFNet_VGG19, "HDFNet_VGG19"),
        "HDFNet_Res50": curve_info(HDFNet_Res50, "HDFNet_Res50"),
        "JLDCF": curve_info(JLDCF, "JLDCF"),
        "CoNet": curve_info(CoNet, "CoNet"),
        "BBSNet": curve_info(BBSNet, "BBSNet"),
        "CMWNet": curve_info(CMWNet, "CMWNet"),
        "FRDT": curve_info(FRDT, "FRDT"),
        "S2MA": curve_info(S2MA, "S2MA"),
        "UCNet": curve_info(UCNet, "UCNet"),
        "UCNet_ABP": curve_info(UCNet_ABP, "UCNet_ABP"),
        "UCNet_CVAE": curve_info(UCNet_CVAE, "UCNet_CVAE"),
        "CasGNN": curve_info(CasGNN, "CasGNN"),
        "DANet_VGG16": curve_info(DANet_VGG16, "DANet_VGG16"),
        "DANet_VGG19": curve_info(DANet_VGG19, "DANet_VGG19"),
        "PGAR": curve_info(PGAR, "PGAR"),
        "DisenFuse": curve_info(DisenFuse, "DisenFuse"),
        "DPANet": curve_info(DPANet, "DPANet"),
        "ICNet": curve_info(ICNet, "ICNet"),
        "D3Net": curve_info(D3Net, "D3Net"),
        "RD3D": curve_info(RD3D, "RD3D"),
        "AFNet": curve_info(AFNet, "AFNet"),
        "CDCP": curve_info(CDCP, "CDCP"),
        "CTMF": curve_info(CTMF, "CTMF"),
        "DCMC": curve_info(DCMC, "DCMC"),
        "DES": curve_info(DES, "DES"),
        "DF": curve_info(DF, "DF"),
        "DMRA": curve_info(DMRA, "DMRA"),
        "MB": curve_info(MB, "MB"),
        "MMCI": curve_info(MMCI, "MMCI"),
        "NLPR": curve_info(NLPR, "NLPR"),
        "PCANet": curve_info(PCANet, "PCANet"),
        "TANet": curve_info(TANet, "TANet"),
    }
)

simple_info = simple_info_generator()
methods_info_for_selecting = OrderedDict(
    {
        "HDFNet_VGG16": simple_info(HDFNet_VGG16, "HDFNet_VGG16"),
        "HDFNet_VGG19": simple_info(HDFNet_VGG19, "HDFNet_VGG19"),
        "HDFNet_Res50": simple_info(HDFNet_Res50, "HDFNet_Res50"),
        "JLDCF": simple_info(JLDCF, "JLDCF"),
        "CoNet": simple_info(CoNet, "CoNet"),
        "BBSNet": simple_info(BBSNet, "BBSNet"),
        "CMWNet": simple_info(CMWNet, "CMWNet"),
        "FRDT": simple_info(FRDT, "FRDT"),
        "S2MA": simple_info(S2MA, "S2MA"),
        "UCNet": simple_info(UCNet, "UCNet"),
        "UCNet_ABP": simple_info(UCNet_ABP, "UCNet_ABP"),
        "UCNet_CVAE": simple_info(UCNet_CVAE, "UCNet_CVAE"),
        "CasGNN": simple_info(CasGNN, "CasGNN"),
        "DANet_VGG16": simple_info(DANet_VGG16, "DANet_VGG16"),
        "DANet_VGG19": simple_info(DANet_VGG19, "DANet_VGG19"),
        "PGAR": simple_info(PGAR, "PGAR"),
        "DisenFuse": simple_info(DisenFuse, "DisenFuse"),
        "DPANet": simple_info(DPANet, "DPANet"),
        "ICNet": simple_info(ICNet, "ICNet"),
        "D3Net": simple_info(D3Net, "D3Net"),
        "RD3D": simple_info(RD3D, "RD3D"),
        "AFNet": simple_info(AFNet, "AFNet"),
        "CDCP": simple_info(CDCP, "CDCP"),
        "CTMF": simple_info(CTMF, "CTMF"),
        "DCMC": simple_info(DCMC, "DCMC"),
        "DES": simple_info(DES, "DES"),
        "DF": simple_info(DF, "DF"),
        "DMRA": simple_info(DMRA, "DMRA"),
        "MB": simple_info(MB, "MB"),
        "MMCI": simple_info(MMCI, "MMCI"),
        "NLPR": simple_info(NLPR, "NLPR"),
        "PCANet": simple_info(PCANet, "PCANet"),
        "TANet": simple_info(TANet, "TANet"),
    }
)
