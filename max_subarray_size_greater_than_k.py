'''array: [-2, 3, 0, 10, -20, 15, 9]
k: 4
subarray max sum and size>=k
'''

def maxsum(array, k):
    if len(array) < k:
        return -1
        
    dic = dict()
    maxsum = 0   
    total = 0
    for index in range(0, len(array)):
        total += array[index]
        dic[index] = total
        
        if index < k -1:
            continue
        if index == k - 1:
            maxsum = max(maxsum, total)
        else:
            maxsum = max(maxsum, total)
            for keys in dic.keys():
                if index - keys > k - 1:
                    maxsum = max(maxsum, total - dic[keys])
    return maxsum
        
array = [-2, 3, 0, 10, -20, 15, 9]
k = 4
print maxsum(array,k)
