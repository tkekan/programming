





def create_table(start, end):
    t = [[0 for x in range(0,end)] for y in range(0,end)]
    for row in range(0,end):
        for col in range(0,end):
            t[row][col] = (row+1) * (col + 1)

    print t


create_table(1,12)
