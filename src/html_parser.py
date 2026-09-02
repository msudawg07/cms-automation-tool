from bs4 import BeautifulSoup

from models import Document, Heading

def parse_html(html: str) -> Document:
  soup = BeautifulSoup(html, "html.parser")

  elements = soup.find_all(recursive=False)

  blocks = []

  for element in elements:
    if element.name in ["h2", "h3"]:
      level = int(element.name[1])
      heading = Heading(text=element.get_text(), level=level)
      blocks.append(heading)

  return Document(blocks=blocks)

html = """
<h3>What is <strong>cholesterol</strong>?</h3>
<p>Cholesterol is a waxy substance.</p>
<h3>What causes high cholesterol?</h3>
"""

print(parse_html(html))
