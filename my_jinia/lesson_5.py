from jinja2 import Environment, FileSystemLoader

file_loader = FileSystemLoader('templates')
env = Environment(loader=file_loader)
tm = env.get_template('head.html')

msg = tm.render(domain='http://yandex.ru', title='про Jinjia')
print(msg)
