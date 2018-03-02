#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import pprint
from itertools import permutations

def test1():
	for i in range(1,5):
		for j in range(1,5):
			for k in range(1,5):
				if (i != k) and (i !=j) and (j!=k):
					print(i,j,k)

def test2():
	d = []
	for i in range(1,5):
		for j in range(1,5):
			for k in range(1,5):
				if(i!=j) and (i!=k) and (j!=k):
					d.append([i, j, k])

	print('总数量：', len(d))
	print(d)

def test3():
	list_num = [1,2,3,4]
	list = [i*100 + j*10 + k for i in list_num for j in list_num for k in list_num if(j!=i and k!=j and k!=i)]
	print(list)

def test4():
	line = []
	for i in range(123,433):
		a = i%10
		b = (i%100)
		c = (i%1000)
		print(a,b,c)
		if a!=b and b!=c and a!=c and 0<a<5 and 0<b<5 and 0<c<5:
			print(i)
			line.append(i)
	print(' the total is: ', len(line))

def test5():
	num = [1,2,3,4]
	i = 0
	for a in num:
		for b in num:
			for c in num:
				if(a!=b) and (b!=c) and (c!=a):
					i += 1
					print(a,b,c)
	print('is total:',i)


def test6():
	list_num = ['1','2','3','4']
	list_result = []
	for i in list_num:
		for j in list_num:
			for k in list_num:
				if len(set(i+j+k)) == 3:
					list_result+=[int(i+j+k)]
	print('is total:%d' % len(list_result))
	print(list_result)
	pprint.pprint(list_result)

def test7():
	for i in permutations([1,2,3,4], 3):
		print(i)

def test8():
	for i in permutations([1,2,3,4], 3):
		k = ''
		for j in range(0,len(i)):
			k = k + str(i[j])
		print(int(k))

def test9():
	for num in range(6,58):
		a = num >> 4 & 3
		b = num >> 2 & 3
		c = num & 3
		if(a^b) and (b^c) and (c^a):
			print(a+1,b+1,c+1)

def test10():
	for i in range(1,5):
		for j in range(1,5):
			if(j==i):
				continue
			for k in range(1,5):
				if(k==i or k==j):
					continue
				print(i,j,k)

def test11():
	list0 = [1,2,3,4]
	list33 = list0.copy()
	for i in list0:
		list1 = list0.copy()
		list1.remove(i)
		for j in list1:
			list2 = list1.copy()
			list2.remove(j)
			for k in list2:
				print(i,j,k)

def test12():
	list_num = [1,2,3,4]
	list = [i*100 +j*10 + k for i in list_num for j in list_num for k in list_num if(i!=j and i!=k and j !=k)]
	print('is total: %d' % len(list))
	print(list)

def test13():
	t = 0
	for i in permutations('1234',3):
		print(''.join(i))
		t+=1
	print('is total %d' % t)

def test14():
	d = []
	for i in range(1,5):
		for j in range(1,5):
			for k in range(1,5):
				if(i!=j!=k!=i):
					d.append(int(str(i)+str(j)+str(k)))
	print(d)
	print(len(d))

def test15():
	d = [(i,j,k) for i in range(1,5) for j in range(1,5) for k in range(1,5) if(i!=j and i!=k and j!=k)]
	print(d)
if __name__ == '__main__':
	# test1()
	# test2()
	# test3()
	# test4()
	# test5()
	# test6()
	# test7()
	# test8()
	# test9()
	# test10()
	# test11()
	# test12()
	# test13()
	# test14()
	test15()