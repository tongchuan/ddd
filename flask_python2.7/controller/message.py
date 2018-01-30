#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from flask import request,render_template,flash,abort,url_for,redirect,session,Flask,g
from main import app,db
from model.User import User
from model.Category import Category
@app.route('/')
def index():
  categorys = Category.query.all()
  return render_template('show_entries.html',entries=categorys)
  # return 'dddddd'

@app.route('/add', methods=['POST'])
def add():
  if not session.get('logged_in'):
    abort(401)
  title = request.form['title']
  content = request.form['text']
  category = Category(title,content)
  db.session.add(category)
  db.session.commit()
  flash('New entry was successfully posted')
  return redirect(url_for('index'))

@app.route('/login',methods=['GET','POST'])
def login():
  error = None
  if request.method == 'POST':
    username = request.form['username']
    password = request.form['password']
    user = User.query.filter_by(username=request.form['username']).first()
    passwd = User.query.filter_by(password=request.form['password']).first()
    print(username,user)
    if user is None:
      error = 'Invalid username'
    elif passwd is None:
      error = 'Invalid password'
    else:
      session['logged_in'] = True
      flash('You were logged in')
      return redirect(url_for('index'))
  return render_template('login.html', error=error)

@app.route('/logout')
def logout():
  session.pop('logged_in', None)
  flash('You were logged out')
  return redirect(url_for('index'))