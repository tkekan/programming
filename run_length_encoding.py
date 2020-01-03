



def encoding(s):
    start = 0
    res = ""
    if len(s) < 2:
        return s
    while start < len(s):
        it = start + 1
        while it <= len(s) - 1 and s[start] == s[it]:
            it+=1
        if it - start == 1:
            res += s[start]
        else:
            res += s[start] + str(it-start)
        start = it
    return res
        



s = "abcccddeeeeea"
s = "aabccdee"
print encoding(s)
