def Order( matrix):
    """
    :type matrix: List[List[int]]
    :rtype: List[int]
    """
    count = len(matrix[0] * len(matrix))
    it = 0
    results = []
    updir = True
    downdir = False
    rows = len(matrix)
    cols = len(matrix[0])
    x = y = 0
    while it != count:
        if updir and x >= 0 and y  < cols:
            results.append(matrix[x][y])
            it += 1
            x = x - 1
            y = y + 1
            continue
        elif downdir == False:
            x = x  + 1
            updir = False
            downdir = True
            if y == cols:
                y = cols - 1
                x = x + 1
            continue
        if downdir and x < rows and y >= 0:
            it += 1
            results.append(matrix[x][y])
            x = x + 1
            y = y - 1
            continue
        else:
            y = y  + 1
            downdir = False
            updir = True
            if x == rows:
                x = rows - 1
                y = y + 1
    return results
array = [
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
#array = [[1],[2],[3],[4],[5],[6],[7],[8],[9],[10]]
results = Order(array)
print results
