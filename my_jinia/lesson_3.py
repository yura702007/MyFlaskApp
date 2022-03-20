from jinja2 import Template

persons = [
    {'name': 'Алексей', 'age': 18, 'weight': 78.5},
    {'name': 'Николай', 'age': 28, 'weight': 82.3},
    {'name': 'Иван', 'age': 33, 'weight': 94.0},
]

html_tm = '''
{%- macro list_users(list_of_users) -%}
<ul>
{%- for u in list_of_users %}
    <li>{{ u.name }}</li>
{%- endfor %}
</ul>
{% endmacro -%}

{{list_users(users)}}
'''

tm = Template(html_tm)
msg = tm.render(users=persons)
print(msg)
'''
{% macro list_users(list_of_user) -%}
<ul>
{% for u in users -%}
    <li>{{u.name}} 
{%- endfor %}
</ul>
{%- endmacro %}

{{list_users(users)}}
'''