#!/usr/bin/env python
# -*- coding: utf-8 -*-
from main import db

class Category(db.Model):
  __tablename__ = 'b_category'
  id = db.Column(db.Integer,primary_key=True)
  title = db.Column(db.String(20),unique=True)
  content = db.Column(db.String(100))

  def __init__(self,title,content):
    self.title = title
    self.content = content
  def __str__(self):
    return '<Category %r>' % self.title

  __repr__ = __str__