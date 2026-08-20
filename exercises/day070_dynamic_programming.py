# Day 70: Dynamic Programming

# Memoized (Top-Down)
def climb_stairs_memo(n: int, memo=None) -> int:
    if memo is None:
        memo = {}
    if n <= 2:
        return n
    if n not in memo:
        memo[n] = climb_stairs_memo(n - 1, memo) + climb_stairs_memo(n - 2, memo)
    return memo[n]

# Tabulated (Bottom-Up)
def climb_stairs_tab(n: int) -> int:
    if n <= 2:
        return n
    dp = [0] * (n + 1)
    dp[1], dp[2] = 1, 2
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]

print("Ways to climb 10 stairs (memo):", climb_stairs_memo(10))
print("Ways to climb 10 stairs (tab): ", climb_stairs_tab(10))
