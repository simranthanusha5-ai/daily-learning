"""Day 345: Morsel-Driven Query Engine."""

class MorselDispatcher:
    def __init__(self, data, morsel_size=10):
        self.data = data
        self.morsel_size = morsel_size
        self.offset = 0

    def get_next_morsel(self):
        if self.offset >= len(self.data):
            return None
        morsel = self.data[self.offset:self.offset + self.morsel_size]
        self.offset += self.morsel_size
        return morsel

if __name__ == "__main__":
    dataset = list(range(25))
    dispatcher = MorselDispatcher(dataset, morsel_size=10)
    m1 = dispatcher.get_next_morsel()
    m2 = dispatcher.get_next_morsel()
    m3 = dispatcher.get_next_morsel()
    assert len(m1) == 10 and len(m3) == 5
    print("Day 345 Morsel Execution tests passed!")
