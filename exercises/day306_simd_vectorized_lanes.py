"""Day 306: SIMD 8-Lane 32-Bit Vector Emulation."""

class SIMDVector8:
    def __init__(self, elements):
        assert len(elements) == 8
        self.lanes = list(elements)

    def __add__(self, other):
        return SIMDVector8([a + b for a, b in zip(self.lanes, other.lanes)])

    def __mul__(self, other):
        return SIMDVector8([a * b for a, b in zip(self.lanes, other.lanes)])

    def horizontal_sum(self):
        return sum(self.lanes)

if __name__ == "__main__":
    v1 = SIMDVector8([1, 2, 3, 4, 5, 6, 7, 8])
    v2 = SIMDVector8([8, 7, 6, 5, 4, 3, 2, 1])
    v_sum = v1 + v2
    assert v_sum.lanes == [9] * 8
    v_dot = (v1 * v2).horizontal_sum()
    assert v_dot == 120
    print("Day 306 SIMD Vector tests passed!")
