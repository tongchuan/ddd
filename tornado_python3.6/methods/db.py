#!/usr/bin/env python
#coding:utf-8

# import MySQLdb



# def select_db():
# 	conn = MySQLdb.connect(host="127.0.0.1", user="root", passwd="root", db="webpython", port=3306, charset="utf8")
# 	# print(conn)
# 	# cur = conn.cursor()
# 	# print(cur)
# 	sql = 'SELECT * FROM `b_category`'
# 	# cur.execute(sql)
# 	# lines = cur.fetchall()
# 	# print(lines)
# 	# return lines

import pymysql

db = pymysql.connect("127.0.0.1","root","root","webpython" )

cursor = db.cursor()

def select_db():
	sql = 'SELECT * FROM `b_category`'
	cursor.execute(sql)
	results = cursor.fetchall()
	# print(results)
	for row in results:
		id = row[0]
		print(str(id)+'ddddd')
		print(row[0])
    # id = row[0]
    # ids = ''
    # title = row[1]
    # content = row[2]
     # 打印结果
    # print ("id=%s,title=%s,content=%s" % \
           # (title, title, content))