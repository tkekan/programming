import sys

def closest(nums):
    preidx = [[0,-1]]
    currsum = 0
    for index in range(len(nums)):
       currsum += nums[index]
       preidx.append([currsum, index])

    preidx.sort(key = lambda x:x[0])
    mindiff = sys.maxint
    for index in range(1,len(preidx)):
        diff = preidx[index][0] - preidx[index-1][0]
        if diff < mindiff:
            start = preidx[index-1][1]    
            end = preidx[index][1]
            mindiff = diff
    
    results =  [start,end]
    results.sort()
    results[0] += 1
    print results

nums = [-3, 1, 1, -3, 5]
closest(nums)
