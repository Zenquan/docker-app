# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     test_decorator
   Description :
   Author :       zenquan
   date：          2019/9/17
-------------------------------------------------
   Change Activity:
                   2019/9/17:
-------------------------------------------------
"""
__author__ = 'zenquan'

def hello(fnc):
    def s_hello():
        print('111')
        fnc()
        print('222')

    return s_hello

@hello
def hi():
    print('333')

hi()