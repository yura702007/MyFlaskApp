from jinja2 import Environment, FileSystemLoader

persons = [
    {'name': 'Алексей', 'age': 18, 'weight': 78.5},
    {'name': 'Николай', 'age': 28, 'weight': 82.3},
    {'name': 'Иван', 'age': 33, 'weight': 94.0}
]

file_loader = FileSystemLoader('templates')  # загрузка директории шаблонов
env = Environment(loader=file_loader)  # создание окружения

tm = env.get_template('main.html')  # загрузка файла шаблона
msg = tm.render(users=persons)
print(msg)
