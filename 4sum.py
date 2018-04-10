def fourSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[List[int]]
    """
    left = 0
    right = 0 
    nums.sort()
    results = []
    for i in range(0,len(nums) -3):
        for j in range(i+1, len(nums) - 2):
            left = j + 1
            right = len(nums) - 1
            while left < right:
                if nums[i] + nums[j] + nums[left] + nums[right] == target:
                    temp = []
                    temp.append(nums[i])
                    temp.append(nums[j])
                    temp.append(nums[left])
                    temp.append(nums[right])
                    results.append(temp)
                    temp = []
                    left+=1
                    right-=1
                elif nums[i] + nums[j] + nums[left] + nums[right] < 0:
                    left+=1
                    while left < right and nums[left] == nums[left - 1]:
                        left+=1
                else:
                    right-=1
                    while left < right and nums[right] == nums[right + 1]:
                        right-=1
                
                    
    
    print results

#nums = [1, 0, -1, 0, -2, 2]
nums = [-3,-2,-1,0,0,1,2,3]
target = 0
fourSum(nums, target)
