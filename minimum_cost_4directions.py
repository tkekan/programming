

def minpath(matrix, r, c, ROWS, COLS):
    if r > ROWS or c > COLS or c < 0:
        return 0

    value = matrix[r][c]
    left = minpath(matrix, r, c - 1, ROWS, COLS)
    right = minpath(matrix, r, c + 1, ROWS, COLS)
    up   = minpath(matrix, r - 1, c, ROWS, COLS)
    bottom - minpath(matrix, r + 1, c , ROWS, COLS)
    return value + min(left, right, up, bottom)


matrix = [[31, 100, 65,12,18],
          [10,13,47,157,6],
          [100,113,174,11,33],
          [88,124,41,20,140],
          [99,32,111,41,20]]

value = minpath(matrix, 0, 0, len(matrix), len(matrix[0]))
print value
