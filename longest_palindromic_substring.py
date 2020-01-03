from pprint import pprint

""" Below is the simplest idea for O(n2) approach where  """

def util( s, left, right):
        slen = len(s)
        
        while left >= 0 and right < slen and s[left] == s[right]:
            left-=1
            right+=1
        
        return right-left-1
    
def longestPalindrome(s):
    
    #:type s: str
    #:rtype: str
    
    if s == None or len(s) == "":
        return "";
    
    end = 0
    start  = 0
    
    for i in range(0,len(s)):
        p1 = util(s, i, i)
        p2 = util(s, i, i+1)
        curr = max(p1,p2)
        if curr > end - start:
            start = i - (curr-1)/2
            end = i+(curr/2)
    
    return s[start:end+1]

"""
def longest(s):
    dp = [[0 for _ in range(len(s))] for _ in range(len(s))]
    l = len(s)
    dp[l-1][l-1] = 1
      # Below need to put 1's in diagonal and at the same time see if 2 len substrings are plaindrome 
      # hence the r range is until l-1 only, so for 8 length string(0-7 index) you traverse only till 6
      #  hence r in range(l-1) 
    maxlen = 0
    for r in range(l-1):
        for c in range(r,r+2):
            if r == c:
                dp[r][c] = 1
            elif s[r] == s[c]:
                dp[r][c] = 1
                maxlen = 2
                res = s[r:c+1]
    
    res = s[0]
    for k in range(2,l):
        for i in range(0,l-1):
            if i + k >= l:
                break
            start,end = i,i+k
            if s[start] == s[end]:
                dp[start][end] = dp[start+1][end-1]
                if dp[start][end] == 1:
                    if end - start + 1 > maxlen:
                        maxlen = end - start + 1
                        res = s[start:end+1]
    print maxlen,res
"""
s = "aaab"
#longest(s)
print longestPalindrome(s)
