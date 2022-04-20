import sqlite3
from flask import Blueprint, request, redirect, url_for, flash, render_template, session, g

admin = Blueprint('admin', __name__, template_folder='templates', static_folder='static')

MENU = [
    {'url': '.index', 'title': 'Панель'},
    {'url': '.logout', 'title': 'Выйти'}
]

db = None


@admin.before_request
def before_request():
    """Установление соединения с БД перед выполнением запроса"""
    global db
    db = g.get('link_db')


@admin.teardown_request
def teardown_request(request):
    global db
    db = None
    return request


def login_admin():
    session['admin_logged'] = 1


def isLogged():
    return True if session.get('admin_logged') else False


def logout_admin():
    session.pop('admin_logged', None)


@admin.route('/')
def index():
    if not isLogged():
        return redirect(url_for('.login'))
    return render_template('admin/index.html', menu=MENU, title='Админ-панель')


@admin.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        if request.form['user'] == 'admin' and request.form['psw'] == '12345':
            login_admin()
            return redirect(url_for('.index'))
        else:
            flash('Неверная пара логин/пароль', 'error')
    return render_template('admin/login.html', title='Админ-панель')


@admin.route('/logout', methods=['POST', 'GET'])
def logout():
    if not isLogged():
        return redirect(url_for('.login'))
    logout_admin()
    return redirect(url_for('.login'))


@admin.route('/list-pubs')
def list_pubs():
    if not isLogged():
        return redirect(url_for('.login'))
    lst = []
    if db:
        try:
            cur = db.cursor()
            cur.execute(f'SELECT title, text, url FROM posts')
            lst = cur.fletchall()
        except sqlite3.Error as e:
            print(f'Ошибка получения статей из БД {e}')
    return render_template('admin/list_pubs', title='Список статей', menu=MENU, lst=lst)
