
from collections import defaultdict

def longest(words):
    if len(words) == 1:
        return 1
    maxlen = 0
    d = dict()
    words.sort(key=len)
    for w in words:
        if len(w) == 1:
            d[w] = 1
        else:
            maxs = 0
            for i in range(len(w)):
                tmp = w[:i] + w[i+1:]
                maxs = max(maxs,max(d.get(w,0),d.get(tmp,0)) + 1)
            d[w] = maxs
            maxlen = max(maxlen,maxs)
    return maxlen
            


words = ["a","b","ba","bca","bda","bdca"]
print longest(words)
