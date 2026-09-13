# Day 94 Project: Unit Converter

class UnitConverter:
    LENGTH_TO_METERS = {"m": 1.0, "km": 1000.0, "cm": 0.01, "mi": 1609.34, "ft": 0.3048}

    @classmethod
    def convert_length(cls, val: float, from_unit: str, to_unit: str) -> float:
        meters = val * cls.LENGTH_TO_METERS[from_unit]
        return meters / cls.LENGTH_TO_METERS[to_unit]

    @staticmethod
    def celsius_to_fahrenheit(c: float) -> float:
        return (c * 9/5) + 32

    @staticmethod
    def fahrenheit_to_celsius(f: float) -> float:
        return (f - 32) * 5/9

print("10 miles in kilometers:", round(UnitConverter.convert_length(10, "mi", "km"), 2))
print("100 Celsius in Fahrenheit:", UnitConverter.celsius_to_fahrenheit(100))
