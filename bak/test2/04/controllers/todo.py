#/usr/bin/env python
#coding=utf-8
import web
from config import settings
from datetime import datetime
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

render = settings.render
db = settings.db
tb = 'todo'
user = 'user'

def get_by_id(id):
  s = db.select(tb, where='id=$id', vars=locals())
  if not s:
    return False
  return s[0]
class New:
  pass

class Finish:
  def GET(self, id):
    todo = get_by_id(id)
    if not todo:
      return render.error('没有这条记录', None)
    i = web.input()
    print i
    status = i.get('status', 'yes')
    if status == 'yes':
      finished = 1
    elif status == 'no':
      finished = 0
    else:
      return render.error('您发起了一个不允许的请求','/')
    db.update(tb, finished=finished, where='id=$id', vars=locals())
    raise web.seeother('/')

class Edit:
  pass
class Delete:
  pass

class Index:
  def GET(self):
    todos1 = db.select(tb, order='finished asc, id asc')
    todos2 = db.select(tb, order='finished asc, id asc')
    return render.index(todos1, todos2)

class AddUser:
  pass

class Login:
  pass

class Admin:
  pass