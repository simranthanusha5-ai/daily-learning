"""Day 194: Quickselect Order Statistics."""
import random

def quickselect(arr, k):
    def select(left, right, k_idx):
        if left == right:
            return arr[left]
        pivot_idx = random.randint(left, right)
        arr[pivot_idx], arr[right] = arr[right], arr[pivot_idx]
        pivot = arr[right]
        store_idx = left
        for i in range(left, right):
            if arr[i] < pivot:
                arr[store_idx], arr[i] = arr[i], arr[store_idx]
                store_idx += 1
        arr[store_idx], arr[right] = arr[right], arr[store_idx]

        if k_idx == store_idx:
            return arr[store_idx]
        elif k_idx < store_idx:
            return select(left, store_idx - 1, k_idx)
        else:
            return select(store_idx + 1, right, k_idx)

    return select(0, len(arr) - 1, k)

if __name__ == "__main__":
    nums = [7, 10, 4, 3, 20, 15]
    assert quickselect(nums, 2) == 7 # 3rd smallest: 3, 4, 7...
    print("Day 194 Quickselect tests passed!")
