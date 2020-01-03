class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        low = 0
        high = len(nums) - 1
        
        while low <= high:
            mid = (low+high)/2
            if nums[mid] == target or nums[low] == target or nums[high] == target:
                return True
            if nums[low] == nums[high]:
                low  += 1
                high -= 1
                continue
            if nums[high] >= nums[mid]:
                if target <= nums[high]: low = mid + 1
                else: high = mid - 1
                continue
            elif nums[low] <= nums[mid]:
                if target >= nums[low]: high = mid - 1
                else: low = mid + 1
        return False

s = Solution()
nums = [2,5,6,0,0,1,2]
nums = [1,1,3,1]
target = 3
print s.search(nums, target)
