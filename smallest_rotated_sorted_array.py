

def minimum_search(nums):
    low = 0
    high = len(nums) - 1
    while low <= high:
        if nums[low] <= nums[high]:
            return nums[low]
        mid = (low + high) / 2
        if nums[mid] >= nums[low]:
            low = mid + 1
        else:
            high = mid

nums = [4,5,0,1,2,3]
print minimum_search(nums)
