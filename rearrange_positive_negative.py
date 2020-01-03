


def rearrange(arr):
    i = 0
    for j in range(len(arr)):
        if arr[j] < arr[i]:
            arr[j],arr[i] = arr[i],arr[j]
            i += 1
    pos = i+1
    neg = 0
    print arr
    n = len(arr)
    while (pos < n and neg < pos and arr[neg] < 0): 
  
        # swapping of arr 
        arr[neg], arr[pos] = arr[pos], arr[neg] 
        pos += 1
        neg += 2
    print arr


arr = [-1, 2, -3, 4, 5, 6, -7, 8, 9] 
rearrange(arr)
