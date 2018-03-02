#!/usr/bin/env python
# -*- coding:utf-8 -*-

import string, random

# 生成所有字母
def all_string():
  print(string.ascii_letters)
  print(string.letters)
# 生成所有的数字
def all_digits():
  print(string.digits)
def all_add():
  print(string.ascii_letters + string.digits)
def rand_str(num, length=7):
  f = open('./Activation_code.txt', 'w')
  for i in range(num):
    chars = string.ascii_letters +  string.digits
    s = [random.choice(chars) for i in range(length)]
    f.write('{0}\n'.format(''.join(s)))
  f.close()
# 生成所有的小写字母
def all_strlower():
  print(string.ascii_lowercase)
  print(string.lowercase)
# 生成所有的大写字母
def all_strupper():
  print(string.ascii_uppercase)
  print(string.uppercase)
# 生成所有的十六进制字符串
def all_hex():
  print(string.hexdigits)
# 生成所有的八进制字符串
def all_oct():
  print(string.octdigits)
# 在C语言中的标点字符的 ASCII 字符的字符串
def all_pun():
  """!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""
  print(string.punctuation)
# 可打印的字符的字符串。这是一个组合的数字、字母、标点符号和空格。
def all_print():
  print(string.printable)
# 包含的所有字符都被视为空格的字符串。在大多数系统上，这包括空格符、 制表符、 换行符、 回车符、 换页符和垂直制表符
def all_white():
  ' \t\n\r\v\f'
  print(string.whitespace)
# print(string.Formatter())

class Person(object):
  name = 'default name'
  def __init__(self, name = ''):
    self.name = name
if __name__=='__main__':
  # all_string()
  # all_digits()
  # all_add()
  # rand_str(300)
  # all_strlower()
  # all_strupper()
  # all_hex()
  # all_oct()
  # all_pun()
  # all_print()
  # all_white()
  me = Person('younger')
  data = [me]
  s = 'my name is {person[0].name:*^30}'
  formatter = string.Formatter()
  # d = formatter.format(s, person = data)
  d = formatter.vformat(s, (), {'person': data})
  print(d)
  for index, item in enumerate(formatter.parse('my name is zhang tong chuan')):
    print(index, item)
