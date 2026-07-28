# Day 47: Two-Pointer Technique

def two_sum_sorted(nums: list[int], target: int) -> tuple[int, int] | None:
    left, right = 0, len(nums) - 1
    while left < right:
        current_sum = nums[left] + nums[right]
        if current_sum == target:
            return left, right
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    return None

sorted_arr = [2, 7, 11, 15, 22]
target_val = 18
indices = two_sum_sorted(sorted_arr, target_val)
print(f"Two Sum for {target_val} in {sorted_arr}: indices {indices}")
