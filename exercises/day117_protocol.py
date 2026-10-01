# Day 117: Protocol and Structural Subtyping
from typing import Protocol, runtime_checkable

@runtime_checkable
class Renderable(Protocol):
    def render(self) -> str:
        ...

class MarkdownWidget:
    def render(self) -> str:
        return "### Markdown Header"

class JsonWidget:
    def render(self) -> str:
        return '{"status": "ok"}'

def display(widget: Renderable):
    print("Rendered:", widget.render())

display(MarkdownWidget())
display(JsonWidget())
assert isinstance(MarkdownWidget(), Renderable)
