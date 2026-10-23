"""Day 280: Wavelet Tree."""

class WaveletNode:
    def __init__(self, arr, lo, hi):
        self.lo = lo
        self.hi = hi
        self.left = None
        self.right = None
        self.pref_count = [0]
        if lo == hi or not arr:
            return
        mid = (lo + hi) // 2
        left_arr, right_arr = [], []
        cnt = 0
        for x in arr:
            if x <= mid:
                left_arr.append(x)
                cnt += 1
            else:
                right_arr.append(x)
            self.pref_count.append(cnt)
        self.left = WaveletNode(left_arr, lo, mid)
        self.right = WaveletNode(right_arr, mid + 1, hi)

    def rank(self, l, r, k):
        if self.lo == self.hi:
            return r - l + 1 if self.lo == k else 0
        mid = (self.lo + self.hi) // 2
        left_r = self.pref_count[r + 1]
        left_l = self.pref_count[l]
        if k <= mid:
            return self.left.rank(left_l, left_r - 1, k) if left_r > left_l else 0
        else:
            right_r = (r + 1) - left_r
            right_l = l - left_l
            return self.right.rank(right_l, right_r - 1, k) if right_r > right_l else 0

if __name__ == "__main__":
    nums = [1, 3, 2, 3, 4, 3, 1, 5]
    wt = WaveletNode(nums, 1, 5)
    assert wt.rank(1, 5, 3) == 3
    assert wt.rank(0, 7, 1) == 2
    print("Day 280 Wavelet Tree tests passed!")
