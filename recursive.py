def recursive(array, r, c, rows, cols):

    if r > rows or c < 0 or c > cols:
        return 0

    value = array[r][c]
    leftdown = recursive(array,r+1,c-1,rows,cols)
    rightdown = recursive(array, r+1,c+1,rows,cols)
    centerdown = recursive(array, r+1,c,rows,cols)
    return value + max(leftdown,rightdown,centerdown)


array = [[1,2,3,4],[5,6,7,8],[9,0,0,1],[10,100,1,1]]
value = recursive(array, 0, 1, 3, 3)
print value
