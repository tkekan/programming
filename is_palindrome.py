
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left = 0
        right = len(s) - 1
        while left < right:
            while left < len(s) and not s[left].isalnum():
                left += 1
            while right >= 0 and not s[right].isalnum():
                right -= 1
            
            if left >= len(s) or right < 0:
                break
            if s[left].lower() != s[right].lower():
                return False
            else:
                left += 1
                right -= 1
        return True

s = Solution()
s_string = "A man, a plan, a canal: Panama"
print s.isPalindrome(s_string)

