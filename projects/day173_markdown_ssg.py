"""Day 173: Mini Markdown to HTML SSG."""
import re

class MiniSSG:
    @staticmethod
    def render(markdown: str, title="Daily Learning") -> str:
        html = markdown
        # Headers
        html = re.sub(r'^# (.*)$', r'<h1></h1>', html, flags=re.MULTILINE)
        html = re.sub(r'^## (.*)$', r'<h2></h2>', html, flags=re.MULTILINE)
        # Bold & Italic
        html = re.sub(r'\*\*(.*?)\*\*', r'<strong></strong>', html)
        html = re.sub(r'\*(.*?)\*', r'<em></em>', html)
        # Links
        html = re.sub(r'\[(.*?)\]\((.*?)\)', r'<a href=""></a>', html)

        return f"""<!DOCTYPE html>
<html>
<head><title>{title}</title><meta charset="utf-8"></head>
<body>
{html}
</body>
</html>"""

if __name__ == "__main__":
    md = "# Hello World\nThis is **bold** and *italic*."
    res = MiniSSG.render(md)
    assert "<h1>Hello World</h1>" in res
    assert "<strong>bold</strong>" in res
    print("Day 173 SSG tests passed!")
