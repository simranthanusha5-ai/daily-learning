# Day 59: Bubble Sort and Selection Sort

def bubble_sort(arr: list[int]) -> list[int]:
    nums = arr.copy()
    n = len(nums)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                swapped = True
        if not swapped:
            break
    return nums

sample = [64, 34, 25, 12, 22, 11, 90]
print("Original:", sample)
print("Bubble sorted:", bubble_sort(sample))
