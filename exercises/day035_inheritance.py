# Day 35: Inheritance and Method Overriding

class Vehicle:
    def __init__(self, brand: str, model: str):
        self.brand = brand
        self.model = model

    def start(self) -> str:
        return f"{self.brand} {self.model} engine started."

class ElectricCar(Vehicle):
    def __init__(self, brand: str, model: str, battery_kwh: int):
        super().__init__(brand, model)
        self.battery_kwh = battery_kwh

    def start(self) -> str:
        base_msg = super().start()
        return f"{base_msg} (Silent EV mode, {self.battery_kwh} kWh battery active)"

tesla = ElectricCar("Tesla", "Model 3", 75)
print(tesla.start())
