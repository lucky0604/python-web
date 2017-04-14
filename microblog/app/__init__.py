#!/usr/bin/env python3
#-*- coding: utf-8 -*-

# @Author: lucky
# @Date:   2017-04-14T22:41:33+08:00
# @Last modified by:   lucky
# @Last modified time: 2017-04-14T22:55:49+08:00



from flask import Flask

app = Flask(__name__)
from app import views
