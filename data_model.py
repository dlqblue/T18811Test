#!/usr/bin/env python3
# -*- coding: utf-8 -*-


data_type_list = [
    'SFR+ 1000lux Rear', 'SFR+ 35lux Rear', 'SFR+ 1000lux Front', 'SFR+ 35lux Front',
    'Flash 1M', 'Flash 2M',
    'Shading Rear', 'Shading Front',
    'Color 1000lux A Rear', 'Color 35lux A Rear', 'Color 1000lux D65 Rear', 'Color 35lux D65 Rear',
    'Color 1000lux A Front', 'Color 35lux A Front', 'Color 1000lux D65 Front', 'Color 35lux D65 Front',
    'DR Rear', 'DR Front',
    'Noise 1000lux Rear', 'Noise 10lux Rear', 'Noise 1000lux Front', 'Noise 10lux Front'
]


read_sfr_line_number = [63, 65, 66]


def init_global_data():    # 初始化
    global _data_dic
    _data_dic = {}


def set_data_dic(key, value):

    _data_dic[key] = value


def get_data_dic():

    return _data_dic
