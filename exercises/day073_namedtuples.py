# Day 73: Namedtuples
from collections import namedtuple

Color = namedtuple("Color", ["r", "g", "b"])
cyan = Color(0, 255, 255)
print(f"Cyan RGB: r={cyan.r}, g={cyan.g}, b={cyan.b}")
