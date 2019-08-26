


class Solution(object):
    
    def util(self, candidates, curr,totalsum,target,arr):
        if totalsum == target:
            newRes = list(arr)
            self.results.append(newRes)
            return
        
        for index in range(curr,len(candidates)):
            if totalsum + candidates[index] <= target:
                arr.append(candidates[index])
                self.util(candidates, index, totalsum + candidates[index], target,arr)
                arr.pop()
            else:
                return


    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        self.results = []
        
        self.util(candidates, 0, 0,target, [])
        print self.results


s = Solution()
candidates = [2,3,6,7]
print s.combinationSum(candidates , 7)
