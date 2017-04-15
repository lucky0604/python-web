# @Author: lucky
# @Date:   2017-04-15T23:42:13+08:00
# @Last modified by:   lucky
# @Last modified time: 2017-04-15T23:44:07+08:00



from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    nickname = db.Column(db.String(64), index = True, unique = True)
    email = db.Column(db.String(128), index = True, unique = True)

    def __repr__(self):
        return '<User %r>' % (self.nickname)
