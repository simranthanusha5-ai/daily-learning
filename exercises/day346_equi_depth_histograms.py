"""Day 346: Equi-Depth Histograms."""

class EquiDepthHistogram:
    def __init__(self, data, num_buckets=4):
        sorted_data = sorted(data)
        n = len(sorted_data)
        self.buckets = []
        step = n // num_buckets
        for i in range(num_buckets):
            lo = sorted_data[i * step]
            hi = sorted_data[(i + 1) * step - 1] if i + 1 < num_buckets else sorted_data[-1]
            self.buckets.append((lo, hi, step))

    def estimate_count(self, low_val, high_val):
        total = 0
        for lo, hi, count in self.buckets:
            if not (hi < low_val or lo > high_val):
                total += count
        return total

if __name__ == "__main__":
    vals = [10, 20, 25, 30, 40, 50, 60, 70]
    hist = EquiDepthHistogram(vals, num_buckets=2)
    est = hist.estimate_count(15, 35)
    assert est >= 4
    print("Day 346 Histogram tests passed!")
