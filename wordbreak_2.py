def util( s, wordDict, d):
    if s in d:
        return d[s]
    if s == '':
        return []
    res = []
    for w in wordDict:
        if len(s) < len(w):
            continue
        if s[:len(w)] != w:
            continue
        if len(s) == len(w):
            res.append(w)
        else:
            rest = util(s[len(w):], wordDict, d)
            for pat in rest:
                pat = w + " " + pat
                res.append(pat)
    d[s] = res
    return res

def wordBreak(s, wordDict):
    """
    :type s: str
    :type wordDict: List[str]
    :rtype: List[str]
    """
    d = {}
    return util(s, wordDict, d)

s = "catsanddog"
w = ["cat", "cats", "and", "sand", "dog"]
print wordBreak(s,w)
