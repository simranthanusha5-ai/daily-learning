# Day 58: Binary Search

def binary_search(nums: list[int], target: int) -> int:
    low, high = 0, len(nums) - 1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

sorted_list = [10, 23, 35, 47, 59, 68, 72, 85, 99]
target = 59
idx = binary_search(sorted_list, target)
print(f"Target {target} found at index: {idx}")
