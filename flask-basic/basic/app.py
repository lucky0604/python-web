# @Author: lucky
# @Date:   2017-04-12T22:27:13+08:00
# @Last modified by:   lucky
# @Last modified time: 2017-04-12T23:15:26+08:00



from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, world'

@app.route('/hello')
def hello():
    return 'This is Hello'

# 给url添加参数
@app.route('/user/<username>')
def show_user_name(username):
    return 'User %s' % username

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # 显示给定id的post，id为int类型
    return 'Post %d' % post_id
