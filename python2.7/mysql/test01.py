#!/usr/bin/env python
# -*- coding: utf-8 -*-

import MySQLdb

conn = MySQLdb.connect(host="127.0.0.1",user="root",passwd="root",db="webpython",port=3306,charset="utf8")

cursor = conn.cursor()

# close()	关闭游标。之后游标不可用
# execute(query[,args])	执行一条 SQL 语句，可以带参数
# executemany(query, pseq)	对序列 pseq 中的每个参数执行 sql 语句
# fetchone()	返回一条查询结果
# fetchall()	返回所有查询结果
# fetchmany([size])	返回 size 条结果
# nextset()	移动到下一个结果
# scroll(value,mode='relative')	移动游标到指定行，如果 mode='relative',则表示从当前所在行移动 value 条,如果 mode='absolute',则表示从结果集的第一行移动 value 条.

def createTable():
  sql = 'create table mysql_users(id int(2) not null primary key auto_increment,username varchar(40),password text,email text)default charset=utf8'
  cursor.execute(sql)
  conn.commit()

def insertData():
  
  # sql="insert into mysql_users(username,password,email) values (%s,%s,%s)",(("google","111222","g@gmail.com"),("facebook","222333","f@face.book"),("github","333444","git@hub.com"),("docker","444555","doc@ker.com"))
  sql="insert into mysql_users(username,password,email) values (%s,%s,%s)",("Python","123456","Python@gmail.com")
  # print(sql)
  result = cursor.execute("insert into mysql_users(username,password,email) values (%s,%s,%s)",("Python","123456","Python@gmail.com"))
  print(result)
  conn.commit()

def insertMoreData():
  result = cursor.executemany("insert into mysql_users (username,password,email) values (%s,%s,%s)",(("google","111222","g@gmail.com"),("facebook","222333","f@face.book"),("github","333444","git@hub.com"),("docker","444555","doc@ker.com")))
  print(result)
  conn.commit()

def selectTable():
  result = cursor.execute("select * from mysql_users")
  print(result)
  data = cursor.fetchall()
  for item in data:
    print(item)

def selectTableOne():
  result = cursor.execute("select * from mysql_users where id=5")
  print(result)
  line_first = cursor.fetchone()     #只返回一条
  print line_first

def selectTableScroll():
  result = cursor.execute("select * from mysql_users")
  print(result)
  cursor.scroll(1)

  # cur.scroll(2,"absolute")    #回到序号是 2,但指向第三条
  data = cursor.fetchall()
  for item in data:
    print(item)

def dictCursorTable():
  cur = conn.cursor(cursorclass=MySQLdb.cursors.DictCursor)
  cur.execute("select * from mysql_users")
  data = cur.fetchall()
  print data

  for item in data:
    for k, v in item.items():
      print k,': ',v
    print item
  
def updateData():
  cursor = conn.cursor(cursorclass=MySQLdb.cursors.DictCursor)
  cursor.execute("select * from mysql_users where id=5")
  print cursor.fetchone()
  cursor.execute("update mysql_users set username=%s where id=5",("mypython",))
  cursor.execute("select * from mysql_users where id=5")
  print cursor.fetchone()
  # conn.commit() 不过，要真的实现在数据库中更新，还要运行：
if __name__=='__main__':
  updateData()
  cursor.close()
  conn.close()
  # dictCursorTable()
  # selectTableOne()
  # selectTable()
  # insertData()
  # insertMoreData()
  # createTable()
  