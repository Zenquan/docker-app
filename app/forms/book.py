# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     book
   Description :
   Author :       zenquan
   date：          2019/9/17
-------------------------------------------------
   Change Activity:
                   2019/9/17:
-------------------------------------------------
"""
__author__ = 'zenquan'

from wtforms import Form, StringField, IntegerField
from wtforms.validators import Length, NumberRange, DataRequired

class SearcgForm(Form):
    q = StringField(validators=[DataRequired(),Length(min=1, max=30, message='q参数错误')])
    page = IntegerField(validators=[NumberRange(min=1, max=99)], default=1)