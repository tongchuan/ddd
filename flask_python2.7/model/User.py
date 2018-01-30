#!/usr/bin/env python
# -*- coding: utf-8 -*-
from main import db

class User(db.Model):
  __tablename__ = 'b_user'
  id = db.Column(db.Integer,primary_key=True)
  username = db.Column(db.String(10),unique=True)
  password = db.Column(db.String(16))

  def __init__(self,username,password):
    self.username  = username
    self.password = password
  def __str__(self):
    return '<User %r>' % self.username

  __repr__ = __str__