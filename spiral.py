

def spiral(m):
    while m:
        print(" ".join(map(str,m[0]))),
        m = m[1:]
        m = zip(*m)[::-1]
        

m = [[1,2,3],[4,5,6],[7,8,9]]
spiral(m)
