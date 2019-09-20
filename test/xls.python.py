# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     xls.python
   Description :
   Author :       zenquan
   date：          2019/9/20
-------------------------------------------------
   Change Activity:
                   2019/9/20:
-------------------------------------------------
"""
__author__ = 'zenquan'

import xlrd

user_info = xlrd.open_workbook('./data.xlsx')
#
# for sheet in user_info.sheets():
#     print(sheet.name)

sheet = user_info.sheet_by_name('用户信息')
# print(sheet.nrows)

for i in range(sheet.nrows):
    print(sheet.row_values(i))
