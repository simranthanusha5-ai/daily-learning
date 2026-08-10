# Day 60: Insertion Sort

def insertion_sort(arr: list[int]) -> list[int]:
    nums = arr.copy()
    for i in range(1, len(nums)):
        key = nums[i]
        j = i - 1
        while j >= 0 and nums[j] > key:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = key
    return nums

print("Insertion sort result:", insertion_sort([12, 11, 13, 5, 6]))
