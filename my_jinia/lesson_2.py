from jinja2 import Template

data = """{% raw %}Модуль jinja вместо
определения {{ name }} 
подставляет соответствующее значение{% endraw %}"""

tm = Template(data)
tmg = tm.render(name='Юрий')
print(tmg)
