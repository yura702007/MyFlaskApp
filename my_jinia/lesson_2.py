from jinja2 import Template

data = """Модуль jinja вместо
определения {{ name }} 
подставляет соответствующее значение"""

tm = Template(data)
tmg = tm.render(name='Юрий')
print(tmg)
