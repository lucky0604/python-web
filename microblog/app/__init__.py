#!/usr/bin/env python3
#-*- coding: utf-8 -*-

# @Author: lucky
# @Date:   2017-04-14T22:41:33+08:00
# @Last modified by:   lucky
# @Last modified time: 2017-04-15T23:41:40+08:00



from flask import Flask
# 初始化数据库
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# 告诉flask去读取以及使用配置文件
app.config.from_object('config')

db = SQLAlchemy(app)

from app import views, models
