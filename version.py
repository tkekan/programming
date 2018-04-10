class Solution(object):
    def compareVersionUtil(self,v1, v2):
        if len(v1) == 0 and len(v2) != 0 and int(v2) != 0: return -1     
        if len(v1) > 0 and int(v1[0]) !=0 and len(v2) == 0: return 1
        if len(v1) == 0 and len(v2) ==0 : return 0
        else: 
            if int(v1[0]) == int(v2[0]):
                ans = self.compareVersionUtil(v1[1:], v2[1:])
                return ans
            elif int(v1[0]) > int(v2[0]):
                return 1
            else: 
                return -1
            
    def compareVersion(self, version1,version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        
        v1 = version1.split('.')
        v2 = version2.split('.')
        answer = self.compareVersionUtil(v1,v2)
        return answer


s1 = Solution()
ans = s1.compareVersion("1.0","01")
print ans,

