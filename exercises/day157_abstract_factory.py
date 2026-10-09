"""Day 157: Abstract Factory Pattern."""
from abc import ABC, abstractmethod

class Button(ABC):
    @abstractmethod
    def render(self): pass

class DarkButton(Button):
    def render(self): return "Dark Button"

class LightButton(Button):
    def render(self): return "Light Button"

class UIFactory(ABC):
    @abstractmethod
    def create_button(self) -> Button: pass

class DarkThemeFactory(UIFactory):
    def create_button(self): return DarkButton()

class LightThemeFactory(UIFactory):
    def create_button(self): return LightButton()

if __name__ == "__main__":
    factory = DarkThemeFactory()
    assert factory.create_button().render() == "Dark Button"
    print("Day 157 Abstract Factory tests passed!")
