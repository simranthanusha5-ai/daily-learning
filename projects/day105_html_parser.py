# Day 105 Project: HTML Link Extractor
from html.parser import HTMLParser

class LinkParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []

    def handle_starttag(self, tag, attrs):
        if tag == "a":
            for attr, val in attrs:
                if attr == "href":
                    self.links.append(val)

html_content = '''
<html>
  <body>
    <h1>Learning Portal</h1>
    <a href="https://github.com">GitHub</a>
    <a href="https://python.org">Python</a>
  </body>
</html>
'''

parser = LinkParser()
parser.feed(html_content)
print("Extracted links:", parser.links)
