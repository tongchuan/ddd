#!/usr/bin/env python
#-*- coding:utf-8 -*-

import os

class Test(object):
	"""docstring for Test"""
	def __init__(self, arg):
		super(Test, self).__init__()
		self.arg = arg

	def main(self):
		print(os.getcwd())
		
if __name__ == '__main__':
	test = Test('arg')
	test.main()