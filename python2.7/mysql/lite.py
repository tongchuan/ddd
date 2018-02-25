#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3

conn = sqlite3.connect('mysql/sqlite2.db')
cur = conn.cursor()

def createTable():
  create_table = "create table books (title text, author text, lang text) "
  cur.execute(create_table)

def insertData():
  result = cur.execute('insert into books values ("from beginner to master", "laoqi", "python")')
  print result
  conn.commit()
def insertDataAll():
  books = [("first book","first","c"), ("second book","second","c"), ("third book","second","python")]
  result = cur.executemany('insert into books values (?,?,?)', books)
  print result
  conn.commit()
def selectData():
  result = cur.execute('select * from books')
  print result
  print result.fetchall()
  print cur.fetchall()

def selectFor():
  rows = cur.execute('select * from books')
  for row in rows:
    print row

def updateData():
  cur.execute("update books set title='physics' where author='first'")
  conn.commit()
  cur.execute("select * from books where author='first'")
  print cur.fetchone()
def deleteData():
  cur.execute("delete from books where author='second'")
  conn.commit()
  cur.execute("select * from books")
  print cur.fetchall()
if __name__=='__main__':
  deleteData()
  # updateData()
  # selectFor()
  # insertDataAll()
  # selectData()
  # insertData()
  # createTable()
  cur.close()
  conn.close()