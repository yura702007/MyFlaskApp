from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'

db = SQLAlchemy(app)


class Users(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    user_email = db.Column(db.String(50), unique=True)
    psw = db.Column(db.String(500), unique=True)
    date = db.Column(db.DateTime, default=datetime.utcnow)


if __name__ == '__main__':
    app.run(debug=True, port=4242)
