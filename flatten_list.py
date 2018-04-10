



def flatten(l):
    while l:
        r = l[0]
        if type(r) == list:
            if len(r) > 1:
                l[0] = l[0][1:]
            else:
                l = l[1:]
            print r[0]
        else:
            print r
            l = l[1:]

flatten([[1,1],2,[3,4]])
