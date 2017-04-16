
#-*- coding: utf-8 -*-

# @Author: lucky
# @Date:   2017-04-14T22:43:01+08:00
# @Last modified by:   lucky
# @Last modified time: 2017-04-15T23:29:17+08:00



from app import app, db, lm, oid
from flask import render_template, flash, redirect, session, url_for, request, g
from flask.ext.login import login_user, logout_user, current_user, login_required
from .forms import LoginForm
from .models import User

# 检查用户是否已经登陆
@app.before_request
def before_request():
    g.user = current_user

# 此函数用于从数据库中加载用户，该函数会被Flask-Login使用
@lm.user_loader
def load_user(id):
    return User.query.get(int(id))


@app.route('/')
@app.route('/index')
@login_required
def index():
    user = g.user
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
@oid.loginhandler
def login():
    if g.user is not None and g.user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    # check the form
    if form.validate_on_submit():
        session['remember_me'] = form.remember_me.data
        return oid.try_login(form.openid.data, ask_for=['nickname', 'email'])
    return render_template('login.html', title = 'Sign in', form = form,
    # 使用配置文件中的openid配置
    providers = app.config['OPENID_PROVIDERS'])

@oid.after_login
def after_login(resp):
    if resp.email is None or resp.email == '':
        flash('Invalid login. Please try again')
        return redirect(url_for('login'))
    user = User.query.filter_by(email = resp.email).first()
    if user is None:
        nickname = resp.nickname
        if nickname is None or nickname == '':
            nickname = resp.email.split('@')[0]
        user = User(nickname=nickname, email=resp.email)
        db.session.add(user)
        db.session.commit()
    remember_me = False

    if 'remember_me' in session:
        remember_me = session['remember_me']
        session.pop('remember_me', None)
    login_user(user, remember = remember_me)
    return redirect(request.args.get('next') or url_for('index'))

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))