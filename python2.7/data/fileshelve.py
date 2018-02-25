#!/usr/bin/env python
# -*- coding: utf-8 -*-

import shelve

def sWrite():
  s = shelve.open('data/db/shelve.db')
  s['name'] = 'www.ztc.com'
  s['lang'] = 'python'
  s['pages'] = 1000
  s['contents'] = {'first':'base knowledge', 'second':'day day up'}
  s.close()

def sRead():
  s = shelve.open('data/db/shelve.db')
  name = s['name']
  print name
  print '==================='
  for k in s:
    print k, s[k]
  print '==================='
  for k, v in s.items():
    print k, v

def keng():
  f = shelve.open('data/db/shelve1.db')
  f['author'] = ['qiwsir']
  # f.close()
  # f = shelve.open('data/db/shelve1.db')
  print f['author']
  f["author"].append("Hetz") #试图增加一个
  print f['author'] #坑就在这里
  f.close()

  f = shelve.open('data/db/shelve2.db', writeback=True)    #多一个参数 True
  f['author'] = ['qiwsir']
  print f['author']
  f["author"].append("Hetz")
  print f['author']
  f.close()
if __name__=='__main__':
  keng()
  # sWrite()
  # sRead()