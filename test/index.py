#!/usr/bin/env python
# encoding: utf-8

"""
@version: v1.0
@author: heqinglin
@license: Apache Licence 
@contact: 237607591@qq.com
@site: http://blog.csdn.net/langtop
@software: PyCharm Community Edition
@file: hello.py
@time: 2017/5/2 16:37
"""

from flask import Flask
from flask import request, render_template

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    newlist = ['湖人横扫火箭', '马刺刺破太阳', '考辛斯含泪转会', '科比即退役最后一战！']
    return render_template('home.html', dict={'name': 'heqinglin'},newlist = enumerate(newlist))


@app.route('/signin', methods=['GET'])
def signin_from():
    return render_template('form.html')
    # return '''<form action='/signin' method = 'POST'>
    #            <p><input name = 'username'></p>
    #            <p><input name = 'password' type='password'></p>
    #            <p><button type='submit'>sign in</button></p>
    #            </form>
    #         '''


@app.route('/signin', methods=['POST'])
def signin():
    print('request:', request.form)
    username = request.form['username']
    password = request.form['password']
    if username == 'admin' and password == 'admin':
        return render_template('signin-ok.html', username=username)
    else:
        return render_template('form.html', message='bad username or password', username=username)


if __name__ == '__main__':
    app.run()
