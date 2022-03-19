from jinja2 import Template

link = """В HTML-документе ссылки определяются так
<a href="#">Ссылка</a>"""

tm = Template('{{ link | e}}')
tmg = tm.render(link=link)
print(tmg)
