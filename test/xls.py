# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     xls
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

userinfo = xlrd.open_workbook('./data.xlsx')
table = userinfo.sheets()[0]
print(table)
# sheet = userinfo.sheet_by_name('用户信息')
# for i in range(sheet.nrows):
#     print(sheet.row_values(i))