def findAnagrams(s, p):
    """
    :type s: str
    :type p: str
    :rtype: List[int]
    """
    hash_p = [0] * 256
    hash_s = [0] * 256
    result = []
    for index in range(0,len(p)):
        hash_p[ord(p[index])] += 1
        hash_s[ord(s[index])] += 1
    end = index + 1
    start = 0
    count = 0
    while end < len(s):
        if hash_s == hash_p:
            result.append(start)
        hash_s[ord(s[start])] -= 1
        start += 1
        hash_s[ord(s[end])] += 1
        end += 1
    if hash_s == hash_p:
        result.append(start)
    return result

s= "cbaebabacd" 
p= "abc"
print findAnagrams(s, p)
        
