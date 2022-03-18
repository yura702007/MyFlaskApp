from jinja2 import Template

# {% %} спецификатор шаблона
# {{ }} выражение для вставки конструкций Python в шаблон
# {# #} блок комментариев
# ## строковый комментарий

name = 'Фёдор'
tm = Template('Привет, {{ name }}')
msg = tm.render(name=name)
msg2 = f'Привет {name}'
print(msg, msg2, sep='\n')
