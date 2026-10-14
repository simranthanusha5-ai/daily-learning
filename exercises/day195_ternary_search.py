"""Day 195: Ternary Search for Extrema."""

def ternary_search_max(f, left, right, eps=1e-7):
    while right - left > eps:
        m1 = left + (right - left) / 3
        m2 = right - (right - left) / 3
        if f(m1) < f(m2):
            left = m1
        else:
            right = m2
    return (left + right) / 2

if __name__ == "__main__":
    # Parabola opening down with max at x = 3
    parabola = lambda x: -(x - 3)**2 + 25
    opt_x = ternary_search_max(parabola, 0, 10)
    assert abs(opt_x - 3.0) < 1e-5
    print("Day 195 Ternary Search tests passed!")
