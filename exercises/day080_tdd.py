# Day 80: TDD Roman Numeral Converter

def int_to_roman(num: int) -> str:
    val_map = [
        (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
        (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
        (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
    ]
    roman = []
    for value, symbol in val_map:
        while num >= value:
            roman.append(symbol)
            num -= value
    return "".join(roman)

assert int_to_roman(1994) == "MCMXCIV"
assert int_to_roman(58) == "LVIII"
print("TDD Roman converter passed assertions!")
