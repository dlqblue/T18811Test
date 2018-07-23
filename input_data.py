#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import win32com.client as win32
import numpy as np
import data_model
import re


def input_sfr_data(wb, obj_data):

    ws = wb.Worksheets('Detail')

