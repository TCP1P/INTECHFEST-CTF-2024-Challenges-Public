import os 
from flask import *
from urllib.parse import quote_plus, unquote_plus
from flask_sqlalchemy import SQLAlchemy

import hashlib

from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__, 
            static_url_path='/assets',
            static_folder='assets',
            template_folder='views')

app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['JSON_SORT_KEYS'] = False

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI')

db = SQLAlchemy(app)

no_session_urls = [
    '/files',
    '/assets'
]

from models.User import User

def sha256(string):
    return hashlib.sha256(string.encode('utf-8')).hexdigest()

@app.before_request
def before_request():
    for url in no_session_urls:
        if request.path.startswith(url):
            return
    
    if 'uid' in session:
        user = User.query.filter_by(id=session['uid']).first()
        if user:
            g.user = user
            return
        else:
            session.pop('uid', None)
            return redirect(url_for('login'))

    path = request.path
    if path.startswith('/login') or path.startswith('/register'):
        return
    
    if path != '/':
        return redirect(url_for('login', url=quote_plus(request.url)))
        
    return redirect(url_for('login'))

@app.route('/')
def index():
    users_count = User.query.count()
    notes_count = Note.query.count()
    my_notes_count = Note.query.filter_by(user_id=session['uid']).count()
    return render_template('dashboard.html', title='Dashboard', users_count=users_count, notes_count=notes_count, my_notes_count=my_notes_count)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "GET":
        return render_template('login.html')

    username = request.form['username']
    password = request.form['password']

    user = User.query.filter_by(username=username, password=sha256(password)).first()
    if user:
        if not user.status == 'active':
            return render_template('login.html', error='Your account has been suspended')
        
        session['uid'] = user.id

        if 'url' in request.args:
            url = request.args['url']
            return redirect(unquote_plus(url))
        
        return redirect(url_for('index'))
    
    return render_template('login.html', error='Invalid username or password')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == "GET":
        return render_template('register.html')

    username = request.form['username']
    password = request.form['password']
    confirm_password = request.form['confirm_password']

    if password != confirm_password:
        return render_template('register.html', error='Password and confirm password does not match')
    
    user = User.query.filter_by(username=username).first()
    if user:
        return render_template('register.html', error='Username already taken')
    
    user = User(username=username, password=sha256(password), role='user', status='active')
    db.session.add(user)
    db.session.commit()

    flash('Your account has been created successfully. Please login to continue.')
    return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session.pop('uid', None)
    return redirect(url_for('index'))

@app.route('/files/<path:path>')
def send_file(path):
    return send_from_directory('files', path)

import setting

from routes.notes import *

if __name__ == '__main__':
    db.reflect()

    app.run()