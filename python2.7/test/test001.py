#!/usr/bin/python 
#coding:utf-8
# -*- doing: UTF-8 -*-
import time;
import json;
import xml;
import _thread
import smtplib
import socket
import sys
import re
import os
import glob
import math
# import date
from datetime import date
from timeit import Timer
import unittest
import urllib
print(dir(os))
# a, b = 0, 1
# while b < 1000:
#   print(b, end=',')
#   a, b = b, a+b
# print(dir(str))
# print(dir(float))
# print(dir(long))
# print(dir(tuple))
# print(dir(dict))
# print(set)
# print(dir(list))
# print(dir(True))
# print(dir(help))
# a, b = 0, 1
# a,b = b,a
# print(a,b)

# lis = [1,2,3,4,5,6,7,8,9,9]
# lis2 =['s','张彤川','a','a','的']
# print(lis)
# print(lis.reverse())
# print(lis)
# print(lis.sort())
# # print(type(lis))
# # print(help(type))
# print(help(list))
# # for x in lis:
# 	print(x)


# help(str)
# string = 'abcdef ghijk limno pqrstuvw xyz'
# print 'capitalize(): '+ string.capitalize()
# print 'str.center():' + string.center(10,'*')
# print 'str.center():' + string.center(40,'*')
# string1 = "菜鸟教程";
# str_utf8 = string1.encode("UTF-8")
# str_gbk = string1.encode("GBK")
# print(string1)
# print("UTF-8 编码：", str_utf8)
# print("GBK 编码：", str_gbk)

# print string
# print string.upper()
# print string.lower()
# print string.capitalize()
# print string.title()
# print '---------------'
# if('H' in string.upper()):
# 	print string[:]
# 	print string[0]
# 	print string[0:4]
# 	print string[:4]
# 	print string[0:]
# 	print string[4:]
# 	print string*3
# if ('H' not in string.upper()):
# 	print '=============='



# print(range(0,256))
# print(xrange(256))



'''
str1 = ''
for x in range(1,256):
	if(int(x)%10==0):
		str1+='\n'
	str1 += '\t\t'+str(x) + ':'+chr(x) + '\t\t'
print(str1)
str1 = ''
for x in xrange(1,256):
	if(int(x)%10==0):
		str1+='\n'
	str1 += '\t\t'+str(x) + ':'+chr(x) + '\t\t'
print(str1)
print(ord('A'))
print u'中文'
print u'中'
print u'\u4e2d'
print u'ABC'.encode('utf-8')
print u'中文'.encode('utf-8')
print len(u'ABC')
print len(u'中文')
print len('\xe4\xb8\xad\xe6\x96\x87')
print '\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8')
print 'Hello %s' % ('张彤川')
print 'Hi, %s, you have $%d.' % ('Michael', 1000000)
print 'Age: %s. Gender: %s' % (25, True)
# %d	整数
# %f	浮点数
# %s	字符串
# %x	十六进制整数
'''

# PI = 3.14159265
# a = 10/3
# print(type(a))

# a = None
# print(type(a))
# print(a)
# a = 1111;
# a = 'abc'
# print(a)

# a = bool
# a = bool(True)
# a = True
# a = -1
# a = 0
# a = 'dssdsd'
# print type(a)
# print type(True) 
# print type(False)


'''
print not True
print not False
if True:
	print True
else:
	print False
'''

#print '''
#my name is zhang
#I am is boy
#okay
#'''

'''
print 'hello \n \t world'
print r'hello \n \t world'
print '\\\n\\'
print r'\\\n\\'
'''
'''
num = 1
num2 = 13433443l
num3 = 3.3
name = raw_input('请输入:')
print type(num)
print type(num2)
print type(num3)
print type(complex(name))
print int(name)
print long(name)
print float(name)
print complex(name)
'''