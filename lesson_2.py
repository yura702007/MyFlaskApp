from flask import Flask, render_template

MENU = ['Установка', 'Первое приложение', 'Обратная связь']

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Про Flask', menu=MENU)


@app.route('/about')
def about():
    return render_template('about.html',  title='О сайте', menu=MENU)


if __name__ == '__main__':
    app.run(debug=True)
