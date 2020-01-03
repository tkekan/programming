def wordBreak(s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        d = dict()
        for w in wordDict:
            d[w] = 1
        dp = [False] * len(s)
        dp[0] = True
        for end in range(1,len(s)+1):
            for start in range(end):
                if dp[start] and s[start:end] in d:
                    dp[end-1] = True
        print dp
        return dp[len(s)-1]


s = "catsandog"
w = ["cats","sand","and","cat"]
#[T, F, F, F, F, F, F, F, F, F]
#s = "leetcode"
#wordDict = ["leet", "code"]
print wordBreak(s,w)
