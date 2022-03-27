from flask import Flask, render_template, url_for

MENU = ['Установка', 'Первое приложение', 'Обратная связь']

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    print(url_for('index'))
    return render_template('index.html', menu=MENU)


@app.route('/about')
def about():
    print(url_for('about'))
    return render_template('about.html', title='О сайте', menu=MENU)


@app.route('/profile/<path:username>')  # int, float
def profile(username):
    return f'Пользователь - {username}'


if __name__ == '__main__':
    # app.run(debug=True)

    with app.test_request_context():
        print(url_for('index'))
        print(url_for('about'))
        print(url_for('profile', username='yury'))
