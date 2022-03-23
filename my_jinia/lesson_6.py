from jinja2 import FileSystemLoader, Environment

file_loader = FileSystemLoader('templates')
env = Environment(loader=file_loader)

template = env.get_template('about.html')
output = template.render()
print(output)
