from jinja2 import Template


# {% %} спецификатор шаблона
# {{ }} выражение для вставки конструкций Python в шаблон
# {# #} блок комментариев
# ## строковый комментарий

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age


person = Person('Юрий', 39)
tm = Template('Привет, мне {{ p.get_age() }} лет и меня зовут {{ p.get_name() }}')
msg = tm.render(p=person)
print(msg)
