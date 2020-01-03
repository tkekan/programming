from collections import defaultdict
def subs(s,k):
    res = set()
    start = 0
    count = defaultdict(int)
    for index in range(len(s)):
        count[s[index]] += 1
        while count[s[index]] > 1:
            count[s[start]] -= 1
            start += 1
        if index - start + 1 == k:
            res.add(s[start:index+1])
            del count[s[start]]
            start += 1
    out = ["wagl", "aglk", "glkn", "lkna", "knag", "gawu", "awun", "wuna", "unag", "nagw", "agwk", "kwag"]
    print res
    assert(len(out) == len(res))





s = "awaglknagawunagwkwagl"
k = 4
subs(s,k)
