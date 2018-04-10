


def paths(matrix, r, c, ROWS, COLS, results):
    if r > ROWS or c > COLS:
        return
    right = paths(matrix, r, c + 1, ROWS, COLS, results)
    down = paths(matrix, r + 1, c, ROWS, COLS, results)

    if r == ROWS and c == COLS :
        results.append(1)

def paths_dp(matrix, r, c, ROWS, COLS):
    dp = [[0 for y in range(0,COLS+1)] for x in range(0, ROWS + 1)] 

path = 0
results = []
matrix = [[1,2,3],[5,6,7],[8,9,10]]
path = paths(matrix, 0, 0, len(matrix) - 1, len(matrix[0]) - 1, results)
print len(results)
