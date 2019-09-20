# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     __init__
   Description :
   Author :       zenquan
   date：          2019/9/16
-------------------------------------------------
   Change Activity:
                   2019/9/16:
-------------------------------------------------
"""
__author__ = 'zenquan'

from flask import Blueprint

web = Blueprint('web', __name__)
from app.web import book