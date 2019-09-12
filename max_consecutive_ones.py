def findMaxConsecutiveOnes(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start = 0
        maxlen = 0
        index = 0
        while index < len(nums):
            if nums[index] == 0:
                while index < len(nums) and nums[index] == 0: 
                    index += 1
                if index >= len(nums):
                    return maxlen
            else:
                start = index
                while index < len(nums) and nums[index] == 1: 
                    index += 1
                maxlen = max(maxlen, index - start)
                if index >= len(nums):
                    return maxlen
        return maxlen

nums = [1,1,0,1,1,1]
print findMaxConsecutiveOnes(nums)
