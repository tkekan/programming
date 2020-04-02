



def counter():
    for x in range(100):
        yield x

res = []
for y in counter():
    if y > 10:
        break
    res.append(y)

print res
res = []
for rest in counter():
    if rest > 20:
        break
    res.append(rest)
print res
