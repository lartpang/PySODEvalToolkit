# -*- coding: utf-8 -*-
from untracked import rgb_cod_methods

from .datasets.rgb_cod import rgb_cod_data
from .datasets.rgb_cosod import rgb_cosod_data
from .datasets.rgb_sod import rgb_sod_data
from .datasets.rgbd_sod import rgbd_sod_data
from .methods import rgb_cosod_methods, rgb_sod_methods, rgbd_sod_methods

total_info = dict(
    rgb_cosod=dict(
        dataset=rgb_cosod_data,
        method=dict(
            drawing=rgb_cosod_methods.methods_info_for_drawing,
            selecting=rgb_cosod_methods.methods_info_for_selecting,
        ),
    ),
    rgb_sod=dict(
        dataset=rgb_sod_data,
        method=dict(
            drawing=rgb_sod_methods.methods_info_for_drawing,
            selecting=rgb_sod_methods.methods_info_for_selecting,
        ),
    ),
    rgb_cod=dict(
        dataset=rgb_cod_data,
        method=dict(
            drawing=rgb_cod_methods.methods_info_for_drawing,
            selecting=rgb_cod_methods.methods_info_for_selecting,
        ),
    ),
    rgbd_sod=dict(
        dataset=rgbd_sod_data,
        method=dict(
            drawing=rgbd_sod_methods.methods_info_for_drawing,
            selecting=rgbd_sod_methods.methods_info_for_selecting,
        ),
    ),
)
