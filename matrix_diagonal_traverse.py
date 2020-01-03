
def inrange(r1,c1,r,c):
    return (r1 >= 0 and c1 < c)

def printDiagonal(mat):
    if not mat:
        return

    r = len(mat)
    c = len(mat[0])
    r1 = 0
    c1 = 0
    ROW=0
    COL=0
    flag = 0
    while True:
        if flag == 0 and r1 < len(mat):
            c1 = 0
            rit = r1
            while inrange(rit,c1,r,c):
                print mat[rit][c1],
                rit -= 1
                c1 += 1
            r1 += 1
            print "\n"
            if r1 == len(mat):
                flag = 1
                r1 -= 1
                c1 = 1
        if flag == 1 and c1 < len(mat[0]):
            cit = c1
            r1 = len(mat)-1
            while inrange(r1,cit,r,c):
                print mat[r1][cit],
                r1 -= 1
                cit += 1
            c1 += 1
            print "\n"
            if c1 == len(mat[0]):
                break

        
        
        



mat = [[1, 2],
       [5, 6]]
printDiagonal(mat)
