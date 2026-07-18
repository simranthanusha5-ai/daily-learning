# Day 37: Polymorphism and Duck Typing

class Square:
    def __init__(self, side: float):
        self.side = side
    def area(self) -> float:
        return self.side ** 2

class Circle:
    def __init__(self, radius: float):
        self.radius = radius
    def area(self) -> float:
        import math
        return math.pi * (self.radius ** 2)

shapes = [Square(4), Circle(3), Square(2.5)]
for shape in shapes:
    print(f"Shape area: {shape.area():.2f}")
