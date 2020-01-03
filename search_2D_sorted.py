

def search(mat,elem):
    if len(mat) ==  1:
        return elem in mat[0]

    r = len(mat) - 1
    c = len(mat[0]) - 1
    rlow = 0
    rhigh = r
    cmid = c/2
    while rlow +1 < rhigh:
        rmid = rlow + ((rhigh - rlow)/2)
        if mat[rmid][cmid] == elem:
            return rmid,cmid
        elif elem < mat[rmid][cmid]:
            rhigh = rmid
        else:
            rlow = rmid

mat = [[0, 6, 8, 9, 11], 
       [20, 22, 28, 29, 31], 
       [36, 38, 50, 61, 63], 
       [64, 66, 100, 122, 128]]

elem = 36
search(mat,elem)
