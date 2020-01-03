


def bubble(array):
    for i in range(0,len(array)-1):
        swapped = False
        for j in range(0,len(array)-i-1):
            if array[j] > array[j+1]:
                swapped = True
                array[j],array[j+1] = array[j+1],array[j]
        if not swapped:
            print "bearking"
            break

    print array


array = [0,1,2,4,5,9,20,10,50,60,100,30,-1]
array = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]
bubble(array)
