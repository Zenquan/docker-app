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

from sqlalchemy import Column,Integer, String
from app.models import db

class Book(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    titile = Column(String(50), nullable=False)
    author = Column(String(30), default='未名')
    isbn = Column(String(15), nullable=False, unique=True)
    pubilsher = Column(String(50))
    price = Column(String(20))
    binding = Column(String(20))
    pages = Column(Integer)
    pubdate = Column(String(20))
    summary = Column(String(1000))
    image = Column(String(50))

    def sample(self):
        pass