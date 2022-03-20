from jinja2 import Template

cars = [
    {'model': 'Ауди', 'price': 23000},
    {'model': 'Шкода', 'price': 17300},
    {'model': 'Вольво', 'price': 44300},
    {'model': 'Опель', 'price': 21300}
]

tpl = "Общая цена автомобилей {{ cs | random }}"
tm = Template(tpl)
msg = tm.render(cs=cars)
print(msg)
