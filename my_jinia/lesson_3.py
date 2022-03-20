from jinja2 import Template

html_tm = '''
{%- macro input(name, value='', type='text', size=50) -%}
    <input type="{{ type }}" name="{{ name }}" value="{{ value|e }}" size="{{ size }}">
{%- endmacro -%}

<p>{{ input('username') }}</p>
<p>{{ input('email') }}</p>
<p>{{ input('password') }}</p>
'''

tm = Template(html_tm)
msg = tm.render()
print(msg)
