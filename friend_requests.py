
from collections import Counter

def friend(ages):
    cnt = Counter()
    for items in ages:
        cnt[items] += 1
        
    total = 0
    for p1 in sorted(cnt,reverse=True):
        for p2 in sorted(cnt,reverse=True):
            if p1 * 0.5 + 7 < p2 <= p1:
                total += cnt[p1] * cnt[p2]
                if p1 == p2:
                    total -= cnt[p1]
    return total

friend([16,17,18])
