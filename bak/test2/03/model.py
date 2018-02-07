#!/usr/bin/env python
#coding=utf-8
import web, datetime
# db = web.database(dbn="mysql",port=3306,db="webpython",user="root",pw="root",host='localhost')
web.db.MySQLDB
# import MySQLdb
# conn = MySQLdb.connect(
#     host = '127.0.0.1',
#     port = 3306,
#     user = 'root',
#     passwd = 'root',
#     db = 'mysql',
#     charset='utf8')
# cur = conn.cursor()
# print cur.execute('select * from user')
# cur.close()
# conn.close()


# def get_posts():
#   conn = MySQLdb.connect(
#     host = '127.0.0.1',
#     port = 3306,
#     user = 'root',
#     passwd = 'root',
#     db = 'mysql',
#     charset='utf8')
#   cur = conn.cursor()
#   cur.execute('SELECT `host`,`user`,`password` FROM `user`')
#   data = cur.fetchall()
#   cur.close()
#   conn.close()
#   return data
  # return cur.execute('select * from entries')
  # return db.select('entries', order='id DESC')
db = web.print(dbn='mysql',port=3306,db="webpython",user="root",pw="root",host='127.0.0.1')
def get_posts():
  return db.select('entries')
  # db.select('entries')
  #db.query('select * from user')
  #print dir(db)
  # db.select('entries')
  # pass


def get_post(id):
  try:
    return db.select('entries', where='id=$id', vars=locals())[0]
  except IndexError:
    return None

def new_post(title, text):
  db.insert('entries', title=title, content=text, posted_on=datetime.datetime.utcnow())

def del_post(id):
  db.delete('entries', where='id=$id', vars=locals())

def update_post(id, title, text):
  db.update('entries', where='id=$id', vars=locals(), title=title, content=text)

def get_text():
  return db.select('text',order='id DESC')

def post_text(text):
  db.insert('text',content=text,posted_on=datetime.datetime.utcnow())