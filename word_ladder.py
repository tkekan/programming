import collections
def ladderLength(beginWord, endWord, wordList):
    """
    :type beginWord: str
    :type endWord: str
    :type wordList: List[str]
    :rtype: int
    """
    
    
    if beginWord == endWord:
        return 0
    
    if beginWord not in wordList:
        wordList.append(beginWord)
    
    d = collections.defaultdict(list)
    q = collections.deque()
    
    for w in wordList:
        for i in range(len(w)):
            tmp = w[:i] + "_" + w[i+1:]
            d[tmp].append(w)
    q.append([beginWord, 1])
    vw = set()
    vw.add(beginWord)
    
    while q:
        word, step = q.popleft()
        if word == endWord:
            return step
        for i in range(len(word)):
            tmp = word[:i] + "_" + word[i+1:]
            for nei in d[tmp]:
                if nei not in vw:
                    vw.add(nei)
                    q.append([nei, step+1])
    return 0
    
beginWord = 'hit'
endWord = 'cog'
wordList = ["hot","dot","dog","lot","log","cog"]
ladderLength(beginWord, endWord, wordList)
