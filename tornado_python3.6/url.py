#!/usr/bim/env python
#coding:utf-8

'''
the url structore of webseite
'''

import imp, sys # utf-8,兼容汉字

imp.reload(sys)
#sys.setdefaultencoding('utf-8')

from handlers.index import IndexHandler 

url = [
	(r'/', IndexHandler)
]