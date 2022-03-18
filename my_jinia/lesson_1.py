from jinja2 import Template

# {% %} спецификатор шаблона
# {{ }} выражение для вставки конструкций Python в шаблон
# {# #} блок комментариев
# ## строковый комментарий


person = {'name': 'Юрий', 'age': 39}
tm = Template('Привет, мне {{ p.age }} лет и меня зовут {{ p.name }}')
msg = tm.render(p=person)
print(msg)
