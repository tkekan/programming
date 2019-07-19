
import heapq

def cutTheSticks(arr):
    while len(arr):
        ele = min(arr)
        count = 0
        index = 0
        while True:
            if index < len(arr):
                arr[index] -= ele
                count += 1
                if arr[index] == 0:
                    arr.pop(index)
                else: 
                    index += 1
            else:
                break
        print count

'''This is faster than above '''
def cutTheSticks2(arr):
    len_ = []
    while arr:
        len_.append(len(arr))
        ele = min(arr)
        temp = []
        for index in range(len(arr)):
            if arr[index] != 0 and arr[index] - ele > 0:
                temp.append(arr[index] - ele)
        arr = temp
    print "cutTheSticks2: " ,len_

def cutTheSticks3(arr):
    h = []
    for items in arr:
        heapq.heappush(h, items)
    result = []
    while len(h):
        result.append(len(h))
        minvalue = heapq.heappop(h)
        while len(h) and h[0] == minvalue:
            heapq.heappop(h)
        for index in range(0,len(h)):
            h[index] -= minvalue
    print result


#arr= [1, 2, 3, 4, 3, 3, 2, 1]
#arr= [5, 4, 4, 2, 2, 8]
#cutTheSticks(arr)
arr= [1, 2, 3, 4, 3, 3, 2, 1]
#arr= [5, 4, 4, 2, 2, 8]
cutTheSticks2(arr)
#arr= [5, 4, 4, 2, 2, 8]
#arr= [1, 2, 3, 4, 3, 3, 2, 1]
#cutTheSticks3(arr)
