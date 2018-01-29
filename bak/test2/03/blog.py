#!/usr/bin/env python
#coding:utf-8

import web
import os
import model
web.config.debug = True
urls = (
  '/', 'Index',
  '/view/(\d+)', 'View',
  '/new', 'New',
  '/delete/(\d+)', 'Delete',
  '/edit/(\d+)', 'Edit',
  '/text','Text',
)

t_globals = {
  'datestr': web.datestr
}

# render = web.template.render('templates/',base='base', globals=t_globals)
# render = web.template.render_cheetah('templates/')
# render = web.template.render(os.path.join(os.path.dirname(__file__),'templates/'),base='base', globals=t_globals)
render = web.template.render('/home/tc/Desktop/python/test2/03/templates/',base='base', globals=t_globals)


# print os.path.join(os.path.dirname(__file__),'templates/')
# print render
class Index:
  def GET(self):
    # return 'ztc'
    # name = 'HELLO'
    # web.header('Content-Type', 'text/html')
    # test = ['dddd']
    # test = web.input(name=None)
    # print test
    # return render.new(test)
    # return render('test.html',{})
    # return 'ddddd'
    posts = model.get_posts()
    # posts = [{'host':'hosthosthost','user':'useruseruser'}]
    # print(posts)
    # return posts
    # return 'ddddd'
    # posts = [{'id':1111,'title':'test','name':'dddd'}]
    return render.index(posts)

class View:
  def GET(self, id):
    post = model.get_post(int(id))
    return render.view(post)

class New:
  form = web.form.Form(
    web.form.Textbox('title', 
      web.form.notnull,
      size=30,
      description='Post title:'),
    web.form.Textarea('content',
      web.form.notnull,
      rows=30, 
      cols=80,
      description="Post content:"),
    web.form.Button('Post entry')
  )
  def GET(self):
    form = self.form()
    return render.new(form)
  def POST(self):
    form = self.form()
    if not form.validates():
      return render.new(form)
    model.new_post(form.d.title, form.d.content)
    raise web.seeother('/')
  
class Delete:
  def POST(self, id):
    model.del_post(int(id))
    raise web.seeother('/')

class Edit:
  def GET(self, id):
    post = model.get_post(int(id))
    form = New.form()
    form.fill(post)
    return render.edit(post, form)
  def POST(self, id):
    form = New.form()
    post = model.get_post(int(id))
    if not form.validates():
      return render.edit(post, form)
    model.update_post(int(id), form.d.title, form.d.content)
    raise web.seeother('/')

class Text:
  form = web.form.Form(
    web.form.Textarea('con',
    description="")
  )
  def GET(self):
    form = self.form()
    return render.text(form)
  def POST(self):
    form = self.form()
    if not form.validates():
      return render.text(form)
    else:
      model.post_text(str(form.d.con))
      return "%s have sent!"%(form.d.con)
    raise web.seeother('/text')

app = web.application(urls, globals())

if __name__=='__main__':
  app.run()