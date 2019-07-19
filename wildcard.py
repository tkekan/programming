def inrange( ind, s):
        return ind < len(s)
        
def isMatch( s, p):
    """
    :type s: str
    :type p: str
    :rtype: bool
    """
    #isMatchutil(s, p, 0, 0, -1)
    pi = 0
    star = -1
    si = 0
    while inrange(si, s):
        if inrange(pi, p):
            if  s[si] == p[pi] or p[pi] == '?':
                si+=1
                pi+=1
                continue
            
            if p[pi] == '*':
                star = pi
                pi+=1
                sp = si
                continue
        if star >= 0:
            sp += 1
            si = sp
            pi = star + 1
            continue
        
        return False
        
    while inrange(pi, p) and p[pi] == '*':
        pi+=1
        
    return pi  == len(p)

s = 'geeksm'
p = 'g*k*m'
ret = isMatch(s, p)
print ret
