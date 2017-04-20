#-*- coding: utf-8 -*-

# @Author: lucky
# @Date:   2017-04-15T23:42:13+08:00
# @Last modified by:   lucky
# @Last modified time: 2017-04-15T23:44:07+08:00



from app import db
from hashlib import md5


class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    nickname = db.Column(db.String(64), index = True, unique = True)
    email = db.Column(db.String(128), index = True, unique = True)
    # add relationship with posts
    posts = db.relationship('Post', backref = 'author', lazy = 'dynamic')
    # about user
    about_me = db.Column(db.String(140))
    # last visiting date
    last_seen = db.Column(db.DateTime)

    # 增加用户头像服务
    def avatar(self, size):
        return 'http://www.gravatar.com/avatar/' + md5(self.email).hexdigest() + '?d=mm&s=' + str(size)

    # 以下方法是Flask-Login扩展需要在User类中实现的特定的方法，但是类如何实现这些方法没有要求

    # 一般而言，这个方法应该只返回 True，除非表示用户的对象因为某些原因不允许被认证。
    def is_authenticated(self):
        return True

    # is_active 方法应该返回 True，除非是用户是无效的，比如因为他们的账号是被禁止
    def is_active(self):
        return True

    # is_anonymous 方法应该返回 True，除非是伪造的用户不允许登录系统
    def is_anonymous(self):
        return False

    # get_id 方法应该返回一个用户唯一的标识符，以 unicode 格式。我们使用数据库生成的唯一的 id
    def get_id(self):
        try:
            return unicode(self.id)    # python 2
        except NameError:
            return str(self.id)    # python 3

    def __repr__(self):
        return '<User %r>' % (self.nickname)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post %r>' % (self.body)
