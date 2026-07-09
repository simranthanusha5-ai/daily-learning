# Day 28: Modules and Namespaces
import math
import sys

def calculate_circle_metrics(radius: float) -> dict:
    """Returns area and circumference of a circle given radius."""
    return {
        "radius": radius,
        "area": math.pi * (radius ** 2),
        "circumference": 2 * math.pi * radius
    }

metrics = calculate_circle_metrics(5.0)
print(f"Radius {metrics['radius']} -> Area: {metrics['area']:.2f}, Circumference: {metrics['circumference']:.2f}")
print("Python executable:", sys.executable)
