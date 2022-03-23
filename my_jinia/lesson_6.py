from jinja2 import FileSystemLoader, Environment

items = ['физика', 'химия', 'математика', 'информатика']

file_loader = FileSystemLoader('templates')
env = Environment(loader=file_loader)

template = env.get_template('about.html')
output = template.render(list_table=items)
print(output)
