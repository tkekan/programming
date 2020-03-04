from collections import defaultdict



def mindel(s):
    d = defaultdict(int)
    for ch in list(s):
        d[ch] += 1

    chset = set()
    dele = 0
    for key,values in d.items():
        if values not in chset:
            chset.add(values)
        else:
            while values in chset and values > 0:
                values -= 1
                dele += 1
            if values > 0:
                chset.add(values)
    print dele
            




s = "aabbffddeaee"
mindel(s)
