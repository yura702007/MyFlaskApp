from jinja2 import Template

cars = [
    {'model': 'Ауди', 'price': 23000},
    {'model': 'Шкода', 'price': 17300},
    {'model': 'Вольво', 'price': 44300},
    {'model': 'Опель', 'price': 21300}
]

tpl = """{% for c in cs -%}
{% filter upper %}{{ c.model }}{% endfilter %}
{% endfor -%}"""
tm = Template(tpl)
msg = tm.render(cs=cars)
print(msg)
