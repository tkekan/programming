import sys


def minJumps(arr, l, h): 
  
    # Base case: when source and 
    # destination are same 
    if (h == l): 
        return 0
  
    # when nothing is reachable  
    # from the given source 
    if (arr[l] == 0): 
        return float('inf') 
  
    # Traverse through all the points  
    # reachable from arr[l]. Recursively  
    # get the minimum number of jumps  
    # needed to reach arr[h] from  
    # these reachable points. 
    min = float('inf') 
    for i in range(l + 1, h + 1): 
        if (i < l + arr[l] + 1): 
            jumps = minJumps(arr, i, h) 
            if (jumps != float('inf') and 
                       jumps + 1 < min): 
                min = jumps + 1
  
    return min


def rec(arr,start, steps):
    if start >= len(arr):
        return steps,False

    if start == len(arr) - 1:
        return steps,True

    if arr[start] <= 0:
        return steps,False

    s = arr[start]
    while s > 0:
        count,ret = rec(arr, start + s, steps+1)
        if ret == True:
            global msteps
            msteps = min(msteps,count)
        s -= 1
    return count,ret
        
    

def minjumps(arr):
    return rec(arr,0,0)

msteps = sys.maxint
arr = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
print minJumps(arr, 0, len(arr)-1)
minjumps(arr)
print msteps

