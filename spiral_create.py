



def create(n):
    matrix = [[0 for x in range(n)] for y in range(n)]
    lr = 0
    hr = n - 1
    lc = 0
    hc = n - 1
    count = 1
    while count <= n * n:
        for index in range(lc,hc+1):
            matrix[lr][index] = count
            count += 1
    
        lr += 1

        for index in range(lr,hr+1):
            matrix[index][hc] = count
            count += 1
    
        hc -= 1

        for index in range(hc,lc-1,-1):
            matrix[hr][index] = count
            count += 1
    
        hr -= 1

        for index in range(hr,lr-1,-1):
            matrix[index][lc] = count
            count += 1
        lc += 1
    print matrix

create(4)
        

