def lengthOfLongestSubstringKDistinct(s, k):
    """
    :type s: str
    :type k: int
    :rtype: int
    """
    start = 0
    dic = dict()
    end = 0
    maxlen = 0
    while end < len(s):
        if len(dic.keys()) <= k:
            dic[s[end]] = dic.get(s[end],0) + 1
            end += 1
        if len(dic.keys()) > k:
            while len(dic.keys()) > k:
                dic[s[start]] -= 1
                if dic[s[start]] == 0:
                    del dic[s[start]]
                start += 1
        maxlen = max(maxlen,end-start)
    return maxlen

s = "eceba"
k = 2
print lengthOfLongestSubstringKDistinct(s,k)
