#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import data_model


def read_sfr(read_file):

    read_line = read_file.readline()
    data_list_dic = {}

    count_line = 0
    n = 1 + 1

    while read_line:

        if data_model.read_sfr_line_number[count_line] == n:

            read_line = read_file.readline().strip()

            data_string = []

            for x in read_line.split(','):
                data_string.append(x)

            if count_line == 0:
                print(data_string[0] + ' CA' + data_string[3])
                data_list_dic[data_string[0]] = data_string[3]

            elif count_line == 1:
                print(data_string[0] + ' CA' + data_string[3])
                data_list_dic[data_string[0]] = data_string[3]

            elif count_line == 2:
                print(data_string[0] + ' MTF50P' + data_string[8])
                data_list_dic['MTF50P'] = data_string[8]

            count_line += 1
            n += 1

            if n > data_model.read_sfr_line_number[-1]:
                break

        else:

            read_line = read_file.readline()
            n += 1

    # 判断两个CA值得大小，找出最大的那个

    a = float(data_list_dic['Worst Pt Wy'])
    b = float(data_list_dic['Worst Cor'])
    worst_data = a if(a > b) else b

    del data_list_dic['Worst Pt Wy']
    del data_list_dic['Worst Cor']

    data_list_dic['CA'] = worst_data

    data_model.set_data_dic('SFR+', data_list_dic)
