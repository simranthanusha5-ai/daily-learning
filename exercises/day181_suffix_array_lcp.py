"""Day 181: Suffix Array and Kasai's LCP."""

def build_suffix_array(s):
    suffixes = sorted([(s[i:], i) for i in range(len(s))])
    return [idx for _, idx in suffixes]

def build_lcp(s, sa):
    n = len(s)
    rank = [0] * n
    for i, suffix_idx in enumerate(sa):
        rank[suffix_idx] = i
    lcp = [0] * n
    k = 0
    for i in range(n):
        if rank[i] == n - 1:
            k = 0
            continue
        j = sa[rank[i] + 1]
        while i + k < n and j + k < n and s[i + k] == s[j + k]:
            k += 1
        lcp[rank[i]] = k
        if k > 0:
            k -= 1
    return lcp

if __name__ == "__main__":
    text = "banana"
    sa = build_suffix_array(text)
    lcp = build_lcp(text, sa)
    assert sa[0] == 5 # 'a'
    assert max(lcp) == 3 # 'ana'
    print("Day 181 Suffix Array & LCP tests passed!")
