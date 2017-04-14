#!/usr/bin/env python3
#-*- coding: utf-8 -*-

# @Author: lucky
# @Date:   2017-04-14T22:43:01+08:00
# @Last modified by:   lucky
# @Last modified time: 2017-04-14T22:58:40+08:00



from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Lucky'}    # 虚拟用户
    posts = [
    {
    'author': {'nickname': 'John'},
    'body': 'Winter is coming'
    },
    {
    'author': {'nickname': 'Susan'},
    'body': 'Sup fresh, our turn baby'
    }
    ]
    return render_template('index.html', title = "Home", user = user, posts = posts)
