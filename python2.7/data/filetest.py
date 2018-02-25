#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cPickle as pickle # cPickle 更快
import StringIO #标准库中的一个模块，跟 file 功能类似，只不过是在内存中操作“文件”

class Book(object):
  def __init__(self, name):
    self.name = name
  def my_book(self):
    print 'my book is: ', self.name

def main():
  pybook = Book("<from beginner to master>")
  pybook.my_book()
  file = StringIO.StringIO()
  pickle.dump(pybook, file, 1)
  # print file.getvalue() #查看“文件”内容，注意下面不是乱码
  # print '--------------------------'
  # pickle.dump(pybook, file)
  # print file.getvalue() 
  file.seek(0)       #找到对应类型 
  pybook2 = pickle.load(file)
  pybook2.my_book()
  file.close()
if __name__=='__main__':
  main()