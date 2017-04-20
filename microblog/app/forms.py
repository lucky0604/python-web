# @Author: lucky
# @Date:   2017-04-15T23:03:28+08:00
# @Last modified by:   lucky
# @Last modified time: 2017-04-15T23:24:52+08:00



from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length

class LoginForm(FlaskForm):
    openid = StringField('openid', validators = [DataRequired()])
    remember_me = BooleanField('remember_me', default = False)

class EditForm(FlaskForm):
    nickname = StringField('nickname', validators = [DataRequired()])
    about_me = TextAreaField('about_me', validators = [Length(min = 0, max = 140)])
