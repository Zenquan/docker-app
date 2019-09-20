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
from flask import Flask
from app.models import db

def create_app():
    app = Flask(__name__, static_folder='view_static')
    app.config.from_object('app.secure')
    app.config.from_object('app.setting')
    register_blueprint(app)

    db.init_app(app)
    with app.app_context():
        db.create_all(app=app)
    return app

def register_blueprint(app):
    from app.web.book import web
    app.register_blueprint(web)