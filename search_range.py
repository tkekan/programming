def searchRange(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    left = 0
    right = len(nums) - 1
    rrange = -1
    lrange = -1
    while left <= right:
        mid = left + ((right-left) / 2)
        if nums[mid] == target and (mid == 0 or nums[mid-1] < target):
            lrange = mid
            break
        elif nums[mid] < target:
            left += 1
        else:
            right -= 1
    if lrange == -1:
        return [lrange,rrange]
    
    left = lrange + 1
    right = len(nums) -1
    
    while left <= right:
        mid = left + ((right - left) / 2)
        if nums[mid] == target and (mid == len(nums)-1 or nums[mid+1] > target):
            rrange = mid
            break
        elif nums[mid] > target:
            right -= 1
        else:
            left += 1
    if rrange == -1:
        rrange = lrange
    return [lrange, rrange]


ret = searchRange([2,2],2)   
print ret
