"""Day 193: Manacher's Algorithm."""

def longest_palindrome(s):
    t = "^#" + "#".join(s) + "#$"
    p = [0] * len(t)
    c = 0
    r = 0
    for i in range(1, len(t) - 1):
        i_mirror = 2 * c - i
        if r > i:
            p[i] = min(r - i, p[i_mirror])
        while t[i + 1 + p[i]] == t[i - 1 - p[i]]:
            p[i] += 1
        if i + p[i] > r:
            c = i
            r = i + p[i]
    max_len = max(p)
    center = p.index(max_len)
    start = (center - max_len) // 2
    return s[start: start + max_len]

if __name__ == "__main__":
    assert longest_palindrome("babad") in ["bab", "aba"]
    assert longest_palindrome("cbbd") == "bb"
    print("Day 193 Manacher's tests passed!")
