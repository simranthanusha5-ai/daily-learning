# Day 41: Custom Iterators

class Countdown:
    def __init__(self, start: int):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        val = self.current
        self.current -= 1
        return val

for count in Countdown(5):
    print(f"T-minus {count}...")
print("Liftoff!")
