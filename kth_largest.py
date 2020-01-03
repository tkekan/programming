

def util(nums, k, start, end):
    if start > end:
        return

    pivot = end
    left = start
    right = end
    while True:
        while nums[left] < nums[pivot] and left < right:
            left += 1
        while nums[right] >= nums[pivot] and right > left:
            right -= 1
        if left == right:
            break
        nums[left],nums[right] = nums[right],nums[left]

    nums[left],nums[pivot] = nums[pivot],nums[left]
    if left +1 == k:
        return nums[left]
    if left + 1 < k:
        return util(nums, k, left + 1, end)
    else:
        return util(nums, k , start, left - 1)

def findkthlargest(nums, k):
    return util(nums, len(nums) - k +1 , 0 , len(nums) - 1)




nums = [1,10,11,12,2]
#2,2,2,1,2,3,1,2]
k = 2
print findkthlargest(nums,k)
