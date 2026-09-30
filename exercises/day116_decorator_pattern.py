# Day 116: Structural Decorator Pattern
from abc import ABC, abstractmethod

class Coffee(ABC):
    @abstractmethod
    def cost(self) -> float:
        pass

class SimpleCoffee(Coffee):
    def cost(self) -> float:
        return 2.50

class MilkDecorator(Coffee):
    def __init__(self, coffee: Coffee):
        self._coffee = coffee
    def cost(self) -> float:
        return self._coffee.cost() + 0.75

class VanillaDecorator(Coffee):
    def __init__(self, coffee: Coffee):
        self._coffee = coffee
    def cost(self) -> float:
        return self._coffee.cost() + 0.50

cup = SimpleCoffee()
cup = MilkDecorator(cup)
cup = VanillaDecorator(cup)
print(f"Total beverage cost: ${cup.cost():.2f}")
