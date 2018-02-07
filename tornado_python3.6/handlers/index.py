#!/usr/bin/env python
#coding:utf-8

import tornado.web
from methods.db import select_db

class IndexHandler(tornado.web.RequestHandler):
	"""docstring for IndexHandler"""
	# def __init__(self):
	# 	pass
	def get(self):
		select_db()
		self.render('index.html')
		# greeting = self.get_argument('greeting', 'Hello')
		# self.write(greeting + ', welcome you to read: www.itdiffer.com')
	def post(self):
		username = self.get_argument("username")
		password = self.get_argument("password")
    # self.write(username)
