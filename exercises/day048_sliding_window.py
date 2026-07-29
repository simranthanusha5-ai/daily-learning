# Day 48: Sliding Window Technique

def max_subarray_sum(nums: list[int], k: int) -> int:
    """Find maximum sum of a contiguous subarray of size k in O(n)."""
    if len(nums) < k:
        return 0
    window_sum = sum(nums[:k])
    max_sum = window_sum
    for i in range(k, len(nums)):
        window_sum += nums[i] - nums[i - k]
        max_sum = max(max_sum, window_sum)
    return max_sum

arr = [2, 1, 5, 1, 3, 2]
k = 3
print(f"Max sum of subarray size {k} in {arr}: {max_subarray_sum(arr, k)}")
