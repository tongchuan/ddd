
from flask import Flask,url_for,render_template,request,make_response,abort,redirect
import sys
from werkzeug import secure_filename
app = Flask(__name__)

@app.route('/')
def index():
  return 'index'
@app.route('/user/<name>')
def username(name):
  return 'User %s' % name
@app.route('/post/<int:post_id>')
def post(post_id):
  return 'Post %d' % post_id
@app.route('/projects/')
def projects():
  print(url_for('projects'))
  return 'The project page'
@app.route('/about')
def about():
  return 'The about page'
@app.route('/method',methods=['GET', 'POST', 'HEAD', 'PUT', 'DELETE', 'OPTIONS'])
def method():
  return 'method'

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
  print(request.method)
  print(request.path)
  # print(request.args.get('q', 's'))
  # http://127.0.0.1:5000/hello/ggg?q=ddd&s=ddgggggg
  print(request.args.get('q'))
  print(request.args.get('s'))
  return render_template('hello.html', name=name)

# with app.request_context(environ):
#   assert request.method == 'POST'

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
  if request.method == 'POST':
    f = request.files['the_file']
    # f.save(sys.path.dirname(__file__)+'/uploaded_file.txt')
    f.save('/var/www/uploads/' + secure_filename(f.filename))

@app.route('/cook')
def getcook():
  username = request.cookies.get('username')
@app.route('/setcook')
def setcook():
  resp = make_response(render_template('hello.html'))
  resp.set_cookie('username', 'the username')
  return resp

@app.errorhandler(404)
def page_not_found(error):
  return render_template('page_not_found.html'), 404

@app.route('/red')
def red():
  return redirect(url_for('redlogin'))

@app.route('/redlogin')
def redlogin():
  abort(401)
    # this_is_never_executed()

app.logger.debug('A value for debugging')
app.logger.warning('A warning occurred (%d apples)', 42)
app.logger.error('An error occurred')

with app.test_request_context():
  print(url_for('index'))
  print(url_for('username',name='zhangtongchuan'))
if __name__ == '__main__':
  # app.run()
  # app.run(host='0.0.0.0')
  # app.debug = True
  # app.run()
  # app.run(debug = True)
  app.run(debug=True,host='0.0.0.0')