from flask import Flask, render_template, request

MENU = [{"name": "Установка", "url": "install-flask"},
        {"name": "Первое приложение", "url": "first-app"},
        {"name": "Обратная связь", "url": "contact"}]

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', menu=MENU)


@app.route('/about')
def about():
    return render_template('about.html',  title='О сайте', menu=MENU)


@app.route('/contact', methods=['POST', 'GET'])
def contact():
    if request.method == 'POST':
        print(request.form)
    return render_template('contact.html',  title='Обратная связь', menu=MENU)


if __name__ == '__main__':
    app.run(debug=True)
