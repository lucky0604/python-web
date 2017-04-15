#!/usr/bin/env python3
#-*- coding: utf-8 -*-

# @Author: lucky
# @Date:   2017-04-14T22:43:01+08:00
# @Last modified by:   lucky
# @Last modified time: 2017-04-15T23:29:17+08:00



from app import app
from flask import render_template, flash, redirect
from .forms import LoginForm

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

# Login view
@app.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    # check the form
    if form.validate_on_submit():
        flash('Login requested for openID = "' + form.openid.data + '" , remember_me = ' + str(form.remember_me.data))
        return redirect('/index')
    return render_template('login.html', title = 'Sign in', form = form,
    # 使用配置文件中的openid配置
    providers = app.config['OPENID_PROVIDERS'])
