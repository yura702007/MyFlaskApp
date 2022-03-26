from flask import Flask

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return 'index'


@app.route('/about')
def about():
    return '<h1>О сайте</h1>'


if __name__ == '__main__':
    app.run(debug=True)
