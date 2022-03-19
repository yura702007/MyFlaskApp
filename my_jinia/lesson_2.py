import markupsafe
from jinja2 import Template

link = """В HTML-документе ссылки определяются так
<a href="#">Ссылка</a>"""

tmg = markupsafe.escape(link)
print(tmg)
