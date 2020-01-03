def findAllConcatenatedWordsInADict(words):
    d = {w:True for w in words}
    wordsSet = set(words)
    def is_valid(chars):
        # check if a string that is comprised entirely of at least 1 shorter words in the given array.
        if not chars: return False
        if chars in d: return True
        for i in range(len(chars)):
            if chars[:i+1] in wordsSet:
                if i == len(chars) -1 or is_valid(chars[i+1:]):
                    d[chars] = True
                    return True
        return False
    
    ans = []
    for word in words:
        for i in range(len(word)):
            if word[:i+1] in wordsSet:
                if is_valid(word[i+1:]):
                    ans.append(word)
                    break
    return ans

words = ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]
print findAllConcatenatedWordsInADict(words)
