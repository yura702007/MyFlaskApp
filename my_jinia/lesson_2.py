import markupsafe
from jinja2 import Template

cities = [
    {'id': 1, 'city': 'Москва'},
    {'id': 5, 'city': 'Тверь'},
    {'id': 7, 'city': 'Минск'},
    {'id': 8, 'city': 'Смоленск'},
    {'id': 11, 'city': 'Калуга'},
]

link = """<select name='cities'>
{% for c in cities %}
    <option value="{{ c.id }}">{{ c.city }}</option>
{% endfor %}
</select>"""

mg = Template(link)
tmg = mg.render(cities=cities)
print(tmg)
