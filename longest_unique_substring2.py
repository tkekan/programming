
def longest(s):
    d = {}
    if not s:
        return 0
    res = 1
    currlen = 0
    for i,ch in enumerate(s):
        if ch not in d:
            currlen += 1
        else:
            res = max(res,currlen)
            currlen = i - d[ch]
        d[ch] = i
    return max(res,currlen)

def longest2(s):
    maxlen = 0
    curlen = 0
    d = {}
    for index in range(len(s)):
        if s[index] not in d:
            curlen += 1
        else:
            if index - d[s[index]] < curlen:
                curlen = index - d[s[index]]
        d[s[index]] = index
        #print curlen,index
        maxlen = max(maxlen,curlen)
    return maxlen


print longest2("tmmzuxt")
