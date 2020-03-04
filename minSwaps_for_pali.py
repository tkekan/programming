

def minswaps(s):
    s = list(s)
    i = 0
    j = k = len(s) - 1
    res = 0
    while  i < j:
        a = s[i]
        b = s[k]
        k = j
        if a != b:
            while s[i] != s[k] and k > i:
                k-=1
            if s[i] == s[k] and k!= i:
                while k < j:
                    s[k],s[k+1] = s[k+1],s[k]
                    k += 1
                    res += 1
                i += 1
                j -= 1
            else:
                s[i],s[i+1] = s[i+1],s[i]
                res += 1
        else:
            i += 1
            j -= 1
    print s
    return res



s = "mamad"
s = "aabb"
s = "ntiin"
print minswaps(s)
