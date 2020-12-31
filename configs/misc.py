# -*- coding: utf-8 -*-
def curve_info_generator():
    line_style_flag = True

    def _template_generator(method_info: dict, method_name: str, line_color: str = None, line_width: int = 2) -> dict:
        nonlocal line_style_flag
        template_info = dict(
            path_dict=method_info,
            curve_setting=dict(
                line_style="-" if line_style_flag else "--",
                line_label=method_name,
                line_width=line_width,
            ),
        )
        if line_color is not None:
            template_info["curve_setting"]["line_color"] = line_color

        line_style_flag = not line_style_flag
        return template_info

    return _template_generator


def simple_info_generator():
    def _template_generator(method_info: dict, method_name: str) -> dict:
        template_info = dict(path_dict=method_info, label=method_name)
        return template_info

    return _template_generator
