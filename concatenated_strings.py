

def concatenate(words):
    visited = [False] * len(words)
    ans = [""]
    
    def dfs(words, index, w):
        if len(w) > len(ans[0]):
            ans[0] = str(w)

        for i in range(len(words)):
            if i != index and visited[i] == False:
                if w[-1] == words[i][0]:
                    visited[i] = True
                    dfs(words,i,w[:-1] + words[i])
                    visited[i] = False
        

    for i in range(len(words)):
        visited[i] = True
        dfs(words,i,words[i])
        visited[i] = False
    print ans,len(ans[0])



words = ["good", "dog", "doog", "xyhhdgy"]
words = ['dad', 'did', 'ded', 'dod', 'dot', 'toad', 'doom', 'mango', 'oscar', 'room', 'master', 'oak', 'kaak', 'uv', 'wxyz']
concatenate(words)
