#Place each number at the correct positions
#If the index is out of range, ignore it. 
def findmissing(nums):
    if not nums:
        return 1
    l = len(nums)
    for i in range(0, l):
        num = nums[i]
        while num > 0 and num <= l and num != nums[nums[i] - 1]:
            tmp = num
            nums[i] = nums[nums[i] - 1]
            nums[num - 1] = tmp
            num = nums[i]
        
    for i in range(0,l):
        if nums[i] != i + 1:
            return i + 1


nums = [3,4,-1,1]
print(findmissing(nums))
