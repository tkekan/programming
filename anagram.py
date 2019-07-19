from collections import defaultdict
ana = ['Tar', 'Arc', 'Elbow', 'State', 'Cider', 'Dusty', 'night', 'inch', 'brag', 'cat',
       'rat', 'car', 'below', 'taste', 'cried', 'study', 'thing', 'ACT', 'CHIN']


def getkey(items):
    d = sum(ord(v) for v in list(items))
    return d

dic = defaultdict(list)
for items in ana:
    key = getkey(items.lower())
    #dic[key] = dic.get(key, []) + [items]
    dic[key].append(items)

print dic
