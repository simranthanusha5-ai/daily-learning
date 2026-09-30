# Day 115: Strategy Pattern
from typing import Callable

def percentage_discount(rate: float) -> Callable[[float], float]:
    return lambda price: price * (1 - rate)

def fixed_discount(rebate: float) -> Callable[[float], float]:
    return lambda price: max(0.0, price - rebate)

class ShoppingCart:
    def __init__(self, amount: float):
        self.amount = amount

    def calculate_total(self, strategy: Callable[[float], float]) -> float:
        return round(strategy(self.amount), 2)

cart = ShoppingCart(120.0)
print("With 20% discount: $", cart.calculate_total(percentage_discount(0.20)))
print("With $15 coupon:   $", cart.calculate_total(fixed_discount(15.0)))
