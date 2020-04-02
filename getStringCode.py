

from collections import defaultdict

def getcode(s):
    ret = 0
    shift = 0
    for ch in s:
        if ch >= 'a' and ch <= 'z':
            shift =  1 << (ord(ch) - ord('a'))
        else:
            shift = 1 << (ord(ch) - ord('A'))
        ret = ret | shift
    return ret


def group(lines):
    res = []
    d = defaultdict(list)
    for w in lines:
         d[getcode(w)].append(w)

    for key,val in d.items():
        res.append(val)
    print res
 


lines = ["Good", "god", "dog", "nap"]
group(lines)

