# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     http
   Description :
   Author :       zenquan
   date：          2019/9/12
-------------------------------------------------
   Change Activity:
                   2019/9/12:
-------------------------------------------------
"""
__author__ = 'zenquan'

import requests
class HTTP:
    @staticmethod
    def get(url, return_json=True):
        r = requests.get(url)
        if r.status_code != 200:
            return {} if return_json else ''
        return r.json() if return_json else r.text
