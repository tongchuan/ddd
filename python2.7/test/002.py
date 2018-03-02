#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import sys

def test01():
  i = int(raw_input('净利润：'))
  arr = [1000000,600000,400000,200000,100000,0]
  rat = [0.01,0.015,0.03,0.05,0.075,0.1]
  r = 0
  for idx in range(0,6):
    if i > arr[idx]:
      r += (i-arr[idx])*rat[idx]
      print((i-arr[idx])*rat[idx])
      i = arr[idx]
  print(r)

def test02():
  reload(sys)
  sys.setdefaultencoding('utf-8')
  x = int(raw_input('净利润：'))
  if x<=100000:
    bonus = x*0.1
    print(u'奖金:',bonus,u'元')
  elif 100001<x<200000:
    bonus = 10000+(x-100000)*0.075
    print(u'奖金:',bonus,u'元')
  elif 200001<x<=400000:
    bonus=10000+7500+(x-200000)*0.05
    print(u'奖金:',bonus,u'元')
  elif 400001<x<=600000:
    bonus=10000+7500+10000+(x-400000)*0.03
    print(u'奖金:',bonus,u'元')
  elif 600001<x<=1000000:
    bonus=10000+7500+10000+6000+(x-600000)*0.015
    print(u'奖金:',bonus,u'元')
  elif 600001<x<=1000000:
    bonus=10000+7500+10000+6000+6000+(x-600000)*0.01
    print(u'奖金:',bonus,u'元')

def test03():
  i = int(raw_input('净利润：'))
  I = [1000000,600000,400000,200000,100000,0]
  r = [0.01,0.015,0.03,0.05,0.075,0.1]
  for j in range(len(I)):
    if i > I[j]:
      b = [0,0,0,0,0,0]
      b[j] = i - I[j]
      for k in range(j+1, len(I)):
        b[k] = I[k-1]
      bonus = sum(map(lambda(i1,i2): i1 * i2,zip(b,r)))
      break
  print('奖金：',bonus)

def test04():
  # ###################### 普通函数 ######################
  # 定义函数（普通方式）
  def func(arg):
    return arg + 1
  # 执行函数
  result = func(123) 
  # ###################### lambda ######################
  # 定义函数（lambda表达式）
  my_lambda = lambda arg : arg + 1
  # 执行函数
  result = my_lambda(123)

def funmap(a):
  print(a)
  return a + 1
def test05():
  li = [11,22,33]
  d = map(funmap, li)
  print(d)
  d2 = map(lambda a: a+1, li)
  print(d2)

def funmap2(a,b):
  print(a,b)
  return a + b
def test06():
  li = [11,22,33]
  sl = [1,2,3]
  d = map(funmap2, li, sl)
  d2 = map(lambda a,b: a+b, li, sl)
  print(d)
  print(d2)

def funcfilter(a):
  print(a)
  return a > 22
def test07():
  li = [11,22,23,33,33,44]
  d = filter(lambda a: a > 22, li)
  d2 = filter(funcfilter, li)
  print(d)
  print(d2)

def funcreduce(a,b):
  print(a,b)
  return a+b
def test08():
  li = [1,2,3,4,5]
  d = reduce(lambda a, b: a+b, li)
  d2 = reduce(lambda a, b: a+b, li, 0)
  d3 = reduce(lambda a, b: a+b, li, 1)
  d4 = reduce(funcreduce, li)
  d5 = reduce(funcreduce, li,0)
  d6 = reduce(funcreduce, li,1)
  print([d,d2,d3,d4,d5,d6])

if __name__ == '__main__':
  # test01()
  # test02()
  # test03()
  # test05()
  # test06()
  # test07()
  test08()