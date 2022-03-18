from jinja2 import Template

# {% %} спецификатор шаблона
# {{ }} выражение для вставки конструкций Python в шаблон
# {# #} блок комментариев
# ## строковый комментарий

name = 'Фёдор'
age = 37
tm = Template('Привет, мне {{ a }} лет и меня зовут {{ n }}')
msg = tm.render(n=name, a=age)
print(msg)
