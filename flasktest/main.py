from flask import Flask, url_for, request,render_template,make_response,redirect
import os
app = Flask(__name__)

@app.route('/')
def index():
  return redirect(url_for('hello'))
  return 'index World!'

@app.route('/hello')
def hello():
  app.logger.debug('A value for debugging')
  app.logger.warning('A warning occurred (%d apples)', 42)
  app.logger.error('An error occurred')
  return 'hello world'

@app.route('/user/<username>')
def show_user_profile(username):
  return 'User %s' % username

@app.route('/post/<int:post_id>')
def show_post(post_id):
  return 'Post %d' % post_id

@app.route('/login',methods=['get','post','HEAD','PUT','DELETE','OPTIONS'])
@app.route('/login/<name>')
def login(name=None):
  return str(name) + request.method

@app.route('/view')
@app.route('/view/<name>')
def view(name='zhangtongchuan'):
  return render_template('view.html', name=name)

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
  if request.method == 'POST':
    f = request.files['the_file']
    f.save('/var/www/uploads/' + secure_filename(f.filename))

@app.route('/cookie')
def cookie():
  pass
  # username = request.cookies.get('username')
  # resp = make_response(render_template(...))
  # resp.set_cookie('username', 'the username')
  # return resp

@app.errorhandler(404)
def page_not_found(error):
  return render_template('page_not_found.html'), 404
  # resp = make_response(render_template('error.html'), 404)
  # resp.headers['X-Something'] = 'A value'
  # return resp


@app.route('/osurandom')
def osurandom():
  return os.urandom(24)

with app.test_request_context():
  print url_for('index',next='/')
  print url_for('hello')
  # print url_for('show_user_profile', username='John Doe')
  print url_for('show_post',post_id=1000)
  url_for('static', filename='style.css')


if __name__=='__main__':
  app.debug = True
  # app.run(debug=True)
  app.run(host='0.0.0.0')