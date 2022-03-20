from jinja2 import Template

persons = [
    {'name': 'Алексей', 'old': 18, 'weight': 78.5},
    {'name': 'Николай', 'old': 28, 'weight': 82.3},
    {'name': 'Иван', 'old': 33, 'weight': 94.0},
]

html_tm = '''
{%- macro list_users(list_of_users) -%}
<ul>
{%- for u in list_of_users %}
    <li>{{ u.name }}</li> {{ caller(u) }}
{%- endfor %}
</ul>
{% endmacro -%}

{% call(user) list_users(users) %}
    <ul>
        <li>Возраст: {{ user.age }}</li>
        <li>Вес: {{ user.weight }}</li>
    </ul>
{%- endcall %}
'''

tm = Template(html_tm)
msg = tm.render(users=persons)
print(msg)
'''
{% call(user) list_users(users) %}
    <ul>
    <li>Возраст: {{ user.age }}</li>
    <li>Вес: {{ user.weight }}</li>
    </ul>
{% endcall %}
'''
