

class Solution(object):
    def print_p(self, index,n,openp, closep):
        if closep == n:
            self.result.append(''.join(self.string))
            return
        
        if openp > closep:
            self.string[index] = ')'
            self.print_p(index+1, n, openp, closep+1)
        if openp < n:
            self.string[index] = '('
            self.print_p(index+1, n, openp+1, closep)

    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        self.result = []
        self.string = [""] * (n * 2)
        self.print_p(0, n, 0, 0)
        return self.result

s = Solution()
print s.generateParenthesis(3)
