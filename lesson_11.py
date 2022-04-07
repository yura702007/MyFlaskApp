from flask import Flask, render_template, make_response

app = Flask(__name__)

menu = [
    {'title': 'Главная', 'url': '/'},
    {'title': 'Добавить статью', 'url': '/add_post'}
]


@app.route('/')
def index():
    return render_template('index.html', menu=menu, post=[])


if __name__ == '__main__':
    app.run(debug=True)
