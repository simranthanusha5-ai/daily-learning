"""Day 278: Sparse Table for RMQ."""
import math

class SparseTable:
    def __init__(self, arr):
        self.n = len(arr)
        if self.n == 0:
            return
        self.k = int(math.log2(self.n)) + 1
        self.st = [[0] * self.n for _ in range(self.k)]
        for i in range(self.n):
            self.st[0][i] = arr[i]
        j = 1
        while (1 << j) <= self.n:
            i = 0
            while (i + (1 << j) - 1) < self.n:
                self.st[j][i] = min(self.st[j - 1][i], self.st[j - 1][i + (1 << (j - 1))])
                i += 1
            j += 1

    def query_min(self, L, R):
        length = R - L + 1
        j = int(math.log2(length))
        return min(self.st[j][L], self.st[j][R - (1 << j) + 1])

if __name__ == "__main__":
    nums = [7, 2, 3, 0, 5, 10, 3, 12, 18]
    st = SparseTable(nums)
    assert st.query_min(0, 4) == 0
    assert st.query_min(4, 7) == 3
    assert st.query_min(7, 8) == 12
    print("Day 278 Sparse Table tests passed!")
