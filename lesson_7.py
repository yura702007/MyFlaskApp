from flask import Flask, render_template, request, flash, session, redirect, url_for

MENU = [{"name": "Установка", "url": "install-flask"},
        {"name": "Первое приложение", "url": "first-app"},
        {"name": "Обратная связь", "url": "contact"}]

app = Flask(__name__)

app.config['SECRET_KEY'] = 'qAWYdkSa9Of8hMXG'


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', menu=MENU)


@app.route('/about')
def about():
    return render_template('about.html', title='О сайте', menu=MENU)


@app.route('/contact', methods=['POST', 'GET'])
def contact():
    if request.method == 'POST':
        if len(request.form['username']) > 2:
            flash('Сообщение отправлено', category='success')
        else:
            flash('УУпссс... Произошла ошибка :(', category='error')
    return render_template('contact.html', title='Обратная связь', menu=MENU)


@app.errorhandler(404)
def page_not_found(error):
    title = 'Страница не найдена'
    return render_template('page404.html', title=title, menu=MENU), 404


@app.route('/login', methods=['POST', 'GET'])
def login():
    if 'user_logged' in session:
        return redirect(url_for('profile', username=session['user_logged']))
    elif request.method == 'POST' and request.form['username'] == 'yury' and request.form['psw'] == '123':
        session['user_logged'] = request.form['username']
        return redirect(url_for('profile', username=session['user_logged']))
    return render_template('login.html', title='Авторизация', menu=MENU)


if __name__ == '__main__':
    app.run(debug=True)
