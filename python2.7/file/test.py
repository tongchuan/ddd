#!/usr/bin/env python
#coding:utf-8


import os

def main():
	fileList = os.listdir(os.getcwd())
	for file in fileList:
		print file
		name, ext = file.split('.')
		if len(name) == 2:
			name='0'+name
		dst = name+'.'+ext
		os.rename(file, dst)


if __name__== '__main__':
	main()