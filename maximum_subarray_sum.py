

def maxsum(arr):
    summ = arr[0]
    results = arr[0]
    for index in range(1,len(arr)):
        summ = max(arr[index], summ + arr[index])
        results = max(results,summ)
    return results

arr= [1,4,-5,5,-2,3,-4]
print maxsum(arr)
