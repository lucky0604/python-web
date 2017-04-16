
#-*- coding: utf-8 -*-

# @Author: lucky
# @Date:   2017-04-14T22:41:33+08:00
# @Last modified by:   lucky
# @Last modified time: 2017-04-15T23:41:40+08:00



from flask import Flask
# 初始化数据库
from flask_sqlalchemy import SQLAlchemy
# 对于登录系统，需要用到flask-login扩展
from flask.ext.login import LoginManager
from flask.ext.openid import OpenID
from config import basedir
import os



app = Flask(__name__)
# 告诉flask去读取以及使用配置文件
app.config.from_object('config')

db = SQLAlchemy(app)


lm = LoginManager()
lm.init_app(app)
# 告知Flask-Login哪个视图允许用户登陆
lm.login_view = 'login'
oid = OpenID(app, os.path.join(basedir, 'tmp'))

from app import views, models
