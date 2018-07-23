#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import win32com.client as win32
import re
import os
import data_model
import input_data
import read_data


# 导入Excel库，用这个方法导入Excel库，可以直接读到win32.constants.xlCenter
excel = win32.gencache.EnsureDispatch('Excel.Application')
# 关闭警告对话框
excel.DisplayAlerts = False


class ObjDataModel(object):

    def __init__(self, data_type, type_index=-1, data_list=None):
        if data_list is None:
            data_list = {}
        self.data_list = data_list
        self.data_type = data_type
        self.type_index = type_index


def read_file(path):

    file_type_list = re.split(r"[\\,_,.]", path)

    # 解析文件名跟字典匹配
    file_type = [x for x in file_type_list[-8:] if x in data_model.data_type_list][0]
    type_index = data_model.data_type_list.index(file_type)
    print('-------------------------------data here-------------------------------')
    print('\nFile: ' + path)

    if type_index <= 3:

        print('This is ' + file_type + ' !\n\n')

        obj_data = ObjDataModel(file_type, type_index)

        with open(path, 'r') as readFile:

            read_data.read_sfr(readFile)

            obj_data.data_list = data_model.get_data_dic()

    elif 3 < type_index <= 5:

        print('This is ' + file_type + ' !\n\n')

    elif 5 < type_index <= 7:

        print('This is ' + file_type + ' !\n\n')

    elif 7 < type_index <= 14:

        print('This is ' + file_type + ' !\n\n')

    elif 14 < type_index <= 16:

        print('This is ' + file_type + ' !\n\n')

    elif 16 < type_index <= 20:

        print('This is ' + file_type + ' !\n\n')


def input_excel(obj_data):

    excel_path = ''

    for file_name in os.listdir(os.getcwd()):
        if os.path.splitext(file_name)[1] == '.xlsx':
            excel_path = os.path.join(os.getcwd(), file_name)

    wb = excel.Workbooks.Open(excel_path)

    if obj_data.type_index <= 3:

        input_data.input_sfr_data(wb, obj_data)

    elif 3 < obj_data.type_index <= 5:

        print('This is ' + obj_data.file_type + ' !\n\n')

    elif 5 < obj_data.type_index <= 7:

        print('This is ' + obj_data.file_type + ' !\n\n')

    elif 7 < obj_data.type_index <= 14:

        print('This is ' + obj_data.file_type + ' !\n\n')

    elif 14 < obj_data.type_index <= 16:

        print('This is ' + obj_data.file_type + ' !\n\n')

    elif 16 < obj_data.type_index <= 20:

        print('This is ' + obj_data.file_type + ' !\n\n')


if __name__ == '__main__':

    data_model.init_global_data()

    txt_path = []

    for x in os.listdir(os.getcwd()):
        if os.path.splitext(x)[1] == '.csv':
            txt_path.append(os.path.join(os.getcwd(), x))

    for x in range(len(txt_path)):
        read_file(txt_path[x])
