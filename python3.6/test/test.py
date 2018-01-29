#!/usr/bin/env python
# -*- coding:utf-8 -*-
from flask import Flask,session,redirect,url_for,escape,request
app = Flask(__name__)
@app.route('/')
def index():
  app.logger.debug('A value for debugging')
  app.logger.warning('A warning occurred (%d apples)', 42)
  app.logger.error('An error occurred')
  if 'username' in session:
    return 'Logged in as %s' % escape(session['username'])
  else:
    return 'You are not logged in'
@app.route('/login',methods=['GET','POST'])
def login():
  if request.method == 'POST':
    session['username'] = request.form['username']
    return redirect(url_for('index'))
  return '''
    <form action="" method="post">
      <p><input type=text name=username>
      <p><input type=submit value=Login>
    </form>
    '''
@app.route('/logout')
def logout():
  session.pop('username', None)
  return redirect(url_for('index'))



app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

if __name__=='__main__':
  app.run(debug=True)