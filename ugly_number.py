

def findUglyNumber(array, n):
    factors = [2,3,5]
    index = 1
    array[index] = True
    for f in factors:
        num = index * f
        num = num * num
        while num < 1690:
            array[num] = True
            num = num + f
    print array
    while n:
        if array[index] == True and index < 1690:
            print "index: %d value: %d" %(index,array[index])
            n -= 1
        index += 1
    print index-1

array = [False] * 1690
findUglyNumber(array, 1352)
