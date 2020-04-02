




def minsteps(l):
    l.sort()
    steps = 0
    res = 0
    for i in range(1,len(l)):
        if l[i] != l[i-1]:
            steps += 1
            res = res + steps
        else:
            res = res + steps
    print res



l = [[5,2,1], [4,5,5,4,2]]
for t in l:
    print "test: ", t
    minsteps(t)
