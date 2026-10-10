"""Day 163: Fast Fourier Transform (FFT)."""
import cmath

def fft(a):
    n = len(a)
    if n <= 1:
        return a
    even = fft(a[0::2])
    odd = fft(a[1::2])
    factor = [cmath.exp(-2j * cmath.pi * k / n) * odd[k] for k in range(n // 2)]
    return [even[k] + factor[k] for k in range(n // 2)] + [even[k] - factor[k] for k in range(n // 2)]

if __name__ == "__main__":
    signal = [1.0, 1.0, 1.0, 1.0]
    transformed = fft(signal)
    assert abs(transformed[0] - 4.0) < 1e-6
    print("Day 163 FFT tests passed!")
