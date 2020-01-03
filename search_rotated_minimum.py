#Search in rotated array minimum with duplicates. 

def minimum(arr):
    l = 0
    r = len(arr) - 1
    if arr[l] < arr[r]:
        return arr[0]
    nums = arr
    while l < r:
        mid = l + ((r-l)/2)
        if nums[l] > nums[mid]:
            r = mid
        elif nums[mid] < nums[r]:
            r -= 1
        else:
            l = mid + 1
    return nums[r]

arr = [3,1,1]
print minimum(arr)
