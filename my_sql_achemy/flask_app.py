from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'

db = SQLAlchemy(app)


class Users(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    user_email = db.Column(db.String(50), unique=True)
    psw = db.Column(db.String(500), nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<users {self.user_id}>"


class Profiles(db.Model):
    col_id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(50), nullable=False)
    age = db.Column(db.Integer)
    city = db.Column(db.String(100))
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))

    def __repr__(self):
        return f'<profiles {self.col_id}>'


@app.route('/')
def index():
    return render_template('index.html', title='Главная')


@app.route('/register', methods=['POST', 'GET'])
def register():
    return render_template('register.html', title='Регистрация')


if __name__ == '__main__':
    app.run(debug=True, port=4242)
