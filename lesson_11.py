from flask import Flask, render_template, make_response

app = Flask(__name__)

menu = [
    {'title': 'Главная', 'url': '/'},
    {'title': 'Добавить статью', 'url': '/add_post'}
]


@app.route('/')
def index():
    content = render_template('index.html', menu=menu, post=[])
    res = make_response(content)
    res.headers['Content-Type'] = 'text/plain'
    return res


if __name__ == '__main__':
    app.run(debug=True)
