from collections import defaultdict


wordd = ["area","lead","wall","lady","ball"]

d = defaultdict(set)

for w in wordd:
    for prefix in (w[:i] for i in range(len(w))):
        d[prefix].add(w)

print d
