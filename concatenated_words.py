



def concat(w):
    seen = set(words for words in w)
    res = []
    for words in w:
        seen.remove(words)
        dp = [False] * (len(words) + 1)
        dp[0] = True
        for i in range(0,len(words)):
            if dp[i] == False:
                continue
            c = ""
            for j in range(i,len(words)):
                c += words[j]
                if c in seen:
                    dp[j+1] = True

        if dp[len(words)] == True:
            res.append(words)
        seen.add(words)

    print res
        

w = ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]
concat(w)
