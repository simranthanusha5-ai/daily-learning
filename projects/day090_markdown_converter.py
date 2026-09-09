# Day 90 Project: Simple Markdown to HTML Converter
import re

def markdown_to_html(md_text: str) -> str:
    lines = md_text.strip().split("\n")
    html_lines = []
    for line in lines:
        line = line.strip()
        if line.startswith("# "):
            html_lines.append(f"<h1>{line[2:]}</h1>")
        elif line.startswith("## "):
            html_lines.append(f"<h2>{line[3:]}</h2>")
        elif line.startswith("- "):
            html_lines.append(f"<li>{line[2:]}</li>")
        elif line:
            line = re.sub(r"\*\*(.*?)\*\*", r"<strong>\1</strong>", line)
            line = re.sub(r"\*(.*?)\*", r"<em>\1</em>", line)
            html_lines.append(f"<p>{line}</p>")
    return "\n".join(html_lines)

sample_md = "# Daily Learning\n## Phase 5\n- **Consistency** is *key*."
print("HTML Output:\n", markdown_to_html(sample_md))
