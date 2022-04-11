import sqlite3
import os
from flask import Flask, render_template, request, g, flash, abort, session, redirect, url_for
from f_data_base import FDataBase
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, login_user, login_required, current_user, logout_user
from user_login import UserLogin

# config
DATABASE = '/tmp/flsite.db'
DEBUG = True
SECRET_KEY = 'fdgfh78@#5?>gfhf89dx,v06k'
USERNAME = 'admin'
PASSWORD = '123'

# create web_application
app = Flask(__name__)
# load config from this module
app.config.from_object(__name__)

# change value DATABASE placing database in current application directory
app.config.update(dict(DATABASE=os.path.join(app.root_path, 'flsite.db')))

dbase = None
login_manager = LoginManager(app)


@login_manager.user_loader
def load_user(user_id):
    print('load user')
    return UserLogin().from_db(user_id, dbase)


@app.before_request
def before_request():
    """
    Establishing a database connection before executing a query
    """
    global dbase
    db = get_db()
    dbase = FDataBase(db)


def connect_db():
    """connect with database"""
    conn = sqlite3.connect(app.config['DATABASE'])
    conn.row_factory = sqlite3.Row
    return conn


def create_db():
    """
    create tables in database
    export in console and run
    """
    db = connect_db()
    with app.open_resource('sq_db.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()
    db.close()


def get_db():
    """Database connection if not already established"""
    if not hasattr(g, 'link_db'):
        g.link_db = connect_db()
    return g.link_db


@app.teardown_appcontext
def close_db(error):
    """Close the connection to the database if it was established"""
    if hasattr(g, 'link_db'):
        g.link_db.close()


@app.route('/')
def index():
    return render_template('index.html', menu=dbase.getMenu(), posts=dbase.getPostsAnonce())


@app.route('/add_post', methods=['POST', 'GET'])
def add_post():
    if request.method == 'POST':
        if len(request.form['name']) > 4 and len(request.form['post']) > 10:
            res = dbase.add_post(request.form['name'], request.form['post'], request.form['url'])
            if not res:
                flash('Ошибка добавления статьи', category='error')
            else:
                flash('Статья добавлена успешно', category='success')
        else:
            flash('Ошибка добавления статьи', category='error')
    return render_template('add_post.html', menu=dbase.getMenu(), title='Добавление статьи')


@app.route("/post/<alias>")
@login_required
def showPost(alias):
    title, post = dbase.getPost(alias)
    if not title:
        abort(404)

    return render_template('post.html', menu=dbase.getMenu(), title=title, post=post)


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = dbase.getUserByEmail(request.form['email'])
        if user and check_password_hash(user['psw'], request.form['psw']):
            userlogin = UserLogin().create(user)
            rm = True if request.form.get('remainme') else False
            login_user(userlogin, remember=rm)
            return redirect(url_for('index'))
        flash('Неверная пара логин/пароль', 'error')
    return render_template('login.html', menu=dbase.getMenu(), title='Авторизация')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        session.pop('_flashes', None)
        if len(request.form['name']) > 4 and len(request.form['email']) > 4 and len(request.form['psw']) > 4 \
                and request.form['psw'] == request.form['psw2']:
            psw = request.form['psw']
            _hash = generate_password_hash(psw)
            res = dbase.addUser(request.form['name'], request.form['email'], _hash)
            if res:
                flash("Вы успешно зарегистрированы", "success")
                return redirect(url_for('login'))
            else:
                flash("Ошибка при добавлении в БД", "error")
        else:
            flash("Неверно заполнены поля", "error")

    return render_template('register.html', menu=dbase.getMenu(), title='Регистрация')


@app.route('/profile')
@login_required
def profile():
    return f"""
<a href="{url_for('logout')}">Выйти из профиля</a>
user info: {current_user.get_id()}"""


@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Вы вышли из аккаунта', 'success')
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(debug=DEBUG, port=4242)
