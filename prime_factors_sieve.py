
MAXN = 100001
def sieve():
    spf = [x for x in range(0,MAXN + 1)]
    for index in range(1, MAXN+1):
        if index % 2 == 0:
            spf[index] = 2
        else:
            spf[index] = index

    for index in range(3, MAXN + 1):
        if spf[index] == index:
            j = index * index
            while j < MAXN:
                spf[j] = index
                j = j + index 
    return spf
    
def primefactors(num): 
    spf = sieve()
    while num != 1:
        print spf[num],
        num = num / spf[num]

print "\nnumber: 12246: "
primefactors(12246)
print "\nnumber: 121: "
primefactors(121)
        
