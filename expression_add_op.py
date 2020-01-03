class Solution(object):
    def util(self, nums, target, res, path, curr, prev):
        if len(nums) == 0:
            if target == curr:
                res.append(path)
            return
        for i in range(len(nums)):
            if i == 0 or nums[0]!= '0':
                val = int(nums[:i+1])
                self.util(nums[i+1:], target, res, path+"+"+nums[:i+1], curr+val, val)
                self.util(nums[i+1:], target, res, path+"-"+nums[:i+1], curr-val, -val)
                self.util(nums[i+1:], target, res, path+"*"+nums[:i+1], curr-prev+prev*val, prev*val)
                
            
    def addOperators(self, nums, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        if nums == None or len(nums) == 0:
            return []
        
        res = []
        for i in range(len(nums)):
            if i == 0 or nums[0]!= '0':
                val = int(nums[:i+1])
                self.util(nums[i+1:], target, res, nums[:i+1], val, val)
        return res

s = Solution()
print s.addOperators("123",6)
