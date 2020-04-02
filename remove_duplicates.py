

def remove(nums):
    start = 0
    for index in range(1,len(nums)):
        if nums[start] != nums[index]:
            start+=1
            nums[start] = nums[index]

    print nums[:start+1]

nums = [1,1,1,2,3,3,4,4,4,5]
remove(nums)
