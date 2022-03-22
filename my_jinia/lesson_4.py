from jinja2 import Environment, FileSystemLoader, FunctionLoader


def load_tmp(path):
    if path == 'index':
        return '''Имя{{u.name}}, возраст {{u.age}}, вес {{u.weight}}'''
    else:
        return '''Данные: {{u}}'''


persons = [
    {'name': 'Алексей', 'age': 18, 'weight': 78.5},
    {'name': 'Николай', 'age': 28, 'weight': 82.3},
    {'name': 'Иван', 'age': 33, 'weight': 94.0}
]

# file_loader = FileSystemLoader('templates')  # загрузка директории шаблонов
file_loader = FunctionLoader(load_tmp)  # загрузка шаблона из функции
env = Environment(loader=file_loader)  # создание окружения

tm = env.get_template('index')  # загрузка файла шаблона
msg = tm.render(u=persons[0])
print(msg)
