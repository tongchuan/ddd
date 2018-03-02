#!/usr/bin/env python
#coding:utf-8

# 内建函数 
# abs()	dict()	help()	min()	setattr()
# all()	dir()	hex()	next()	slice()
# any()	divmod()	id()	object()	sorted()
# ascii()	enumerate()	input()	oct()	staticmethod()
# bin()	eval()	int()	open()	str()
# bool()	exec()	isinstance()	ord()	sum()
# bytearray()	filter()	issubclass()	pow()	super()
# bytes()	float()	iter()	print()	tuple()
# callable()	format()	len()	property()	type()
# chr()	frozenset()	list()	range()	vars()
# classmethod()	getattr()	locals()	repr()	zip()
# compile()	globals()	map()	reversed()	__import__()
# complex()	hasattr()	max()	round()	
# delattr()	hash()	memoryview()	set()	

# abs(x)
# 返回一个数的绝对值。参数可以是整数或浮点数。如果参数是一个复数，则返回其大小。
def m_abs():
  print(abs(1))
  print(abs(-1))
  print(abs(1.1111))
  print(abs(-1.1111))
  print(abs(1.1111e10))
  print(abs(-1.1111e7))
  # 1
  # 1
  # 1.1111
  # 1.1111
  # 11111000000.0
  # 11111000.0

# all(iterable)
# 如果iterable中所有的元素都为True，或iterable为空（empty），返回True。等同于：
def m_all():
  a = []  
  b = {1:2, 2:3}  
  c = (1, 3, '', 5)  
  d = [1, 2, None]
  print('a:', all(a), 'b:', all(b), 'c:', all(c), 'd:', all(d))  
  # ('a:', True, 'b:', True, 'c:', False, 'd:', False)

# any(iterable)
# 如果iterable里任何一个元素为True，返回 True。如果iterable为空（empty）,返回 False。等同于：
def m_any():
  a = []  
  b = {1:2, 2:3}  
  c = (1, 3, '', 5)  
  d = [1, 2, None]
  print('a:', any(a), 'b:', any(b), 'c:', any(c), 'd:', any(d))  
  # ('a:', False, 'b:', True, 'c:', True, 'd:', True)



def main():
  # m_abs()
  # m_all()
  # m_any()
  

if __name__ =='__main__':
  main()