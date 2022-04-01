import sqlite3
import os
from flask import Flask, render_template, request, g
from f_data_base import FDataBase

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


@app.route('/index')
def index():
    db = get_db()
    return render_template('index.html', menu=[])


if __name__ == '__main__':
    app.run(debug=True)
