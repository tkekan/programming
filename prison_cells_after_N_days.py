

def post(cells, N):
    ncells = [0] * len(cells)
    d = dict()
    while N > 0:
        for i in range(1,len(cells)-1):
            ncells[i] = (0,1)[cells[i-1] == cells[i+1]]
        N-=1
        cells = list(ncells)

cells = [0,1,0,1,1,0,0,1]
N = 7
post(cells, N)
