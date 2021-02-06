# -*- coding: utf-8 -*-
import os
from collections import OrderedDict

_RGBD_SOD_ROOT = "/home/lart/Datasets/Saliency/RGBDSOD"

LFSD = dict(
    root=os.path.join(_RGBD_SOD_ROOT, "LFSD"),
    image=dict(path=os.path.join(_RGBD_SOD_ROOT, "LFSD", "Image"), suffix=".jpg"),
    mask=dict(path=os.path.join(_RGBD_SOD_ROOT, "LFSD", "Mask"), suffix=".png"),
)
NLPR = dict(
    root=os.path.join(_RGBD_SOD_ROOT, "NLPR_FULL"),
    image=dict(path=os.path.join(_RGBD_SOD_ROOT, "NLPR_FULL", "Image"), suffix=".jpg"),
    mask=dict(path=os.path.join(_RGBD_SOD_ROOT, "NLPR_FULL", "Mask"), suffix=".png"),
    # index_file=os.path.join(_RGBD_SOD_ROOT, "nlpr_test_jw_name_list.lst"),
    # 测试的时候应该使用全部数据来和方法的预测结果计算交集，这样才会测到所有的预测结果，所以就不使用index_file了。
)
NJUD = dict(
    root=os.path.join(_RGBD_SOD_ROOT, "NJUD_FULL"),
    image=dict(path=os.path.join(_RGBD_SOD_ROOT, "NJUD_FULL", "Image"), suffix=".jpg"),
    mask=dict(path=os.path.join(_RGBD_SOD_ROOT, "NJUD_FULL", "Mask"), suffix=".png"),
    # index_file=os.path.join(_RGBD_SOD_ROOT, "njud_test_jw_name_list.lst"),
    # 同上
)
RGBD135 = dict(
    root=os.path.join(_RGBD_SOD_ROOT, "RGBD135"),
    image=dict(path=os.path.join(_RGBD_SOD_ROOT, "RGBD135", "Image"), suffix=".jpg"),
    mask=dict(path=os.path.join(_RGBD_SOD_ROOT, "RGBD135", "Mask"), suffix=".png"),
)
SIP = dict(
    root=os.path.join(_RGBD_SOD_ROOT, "SIP"),
    image=dict(path=os.path.join(_RGBD_SOD_ROOT, "SIP", "Image"), suffix=".jpg"),
    mask=dict(path=os.path.join(_RGBD_SOD_ROOT, "SIP", "Mask"), suffix=".png"),
)
SSD = dict(
    root=os.path.join(_RGBD_SOD_ROOT, "SSD"),
    image=dict(path=os.path.join(_RGBD_SOD_ROOT, "SSD", "Image"), suffix=".jpg"),
    mask=dict(path=os.path.join(_RGBD_SOD_ROOT, "SSD", "Mask"), suffix=".png"),
)
STEREO797 = dict(
    root=os.path.join(_RGBD_SOD_ROOT, "STEREO797"),
    image=dict(path=os.path.join(_RGBD_SOD_ROOT, "STEREO797", "Image"), suffix=".jpg"),
    mask=dict(path=os.path.join(_RGBD_SOD_ROOT, "STEREO797", "Mask"), suffix=".png"),
)
STEREO1000 = dict(
    root=os.path.join(_RGBD_SOD_ROOT, "STEREO1000"),
    image=dict(path=os.path.join(_RGBD_SOD_ROOT, "STEREO1000", "Image"), suffix=".jpg"),
    mask=dict(path=os.path.join(_RGBD_SOD_ROOT, "STEREO1000", "Mask"), suffix=".png"),
)
DUTRGBD_TE = dict(
    root=os.path.join(_RGBD_SOD_ROOT, "DUT-RGBD/Test"),
    image=dict(path=os.path.join(_RGBD_SOD_ROOT, "DUT-RGBD/Test", "Image"), suffix=".jpg"),
    mask=dict(path=os.path.join(_RGBD_SOD_ROOT, "DUT-RGBD/Test", "Mask"), suffix=".png"),
)
RGBDSOD_TR = dict(
    root=os.path.join(_RGBD_SOD_ROOT),
    index_file=os.path.join(_RGBD_SOD_ROOT, "rgbd_train_jw_name_list.lst"),
)

rgbd_sod_data = OrderedDict(
    {
        "LFSD": LFSD,
        "NJUD": NJUD,
        "NLPR": NLPR,
        "RGBD135": RGBD135,
        "SIP": SIP,
        "SSD": SSD,
        "STEREO797": STEREO797,
        "STEREO1000": STEREO1000,
        "DUTRGBD": DUTRGBD_TE,
    }
)
