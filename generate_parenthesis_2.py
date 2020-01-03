
class Solution(object):
    def util(self, lc,rc):
        if lc == 0 and rc == 0:
            self.ans.append(''.join(self.res))
            print self.res
            return
        
        if lc != 0:
            self.res.append('(')
            self.util(lc-1,rc)
            self.res.pop()
            
        if lc > rc:
            self.res.append(')')
            self.util(lc,rc-1)
            self.res.pop()

    def printparen(self,n):
        self.ans = []
        self.res = []
        self.util(n,n)
        print self.ans

s = Solution()
s.printparen(3)
