from collections import defaultdict
class Solution(object):
    
    def graphutil(self,g,stack,node):
        #print "processing %s" % node
        self.visited[ord(node)-ord('a')] = True
        for items in g[node]:
            print "checkiinig in %s %s" %(g[node],node)
            if self.visited[ord(items)-ord('a')] == False:
                self.graphutil(g,stack,items)
        stack.append(node)
    
    def getidx(self,ch):
        return ord(ch) - ord('a')
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        self.visited = [-1] * 26
        g = defaultdict(list)
        for word in words:
            for ch in word:
                idx = self.getidx(ch)
                self.visited[idx] = 0
                
        
        stack = []
        for i in range(1,len(words)):
            word1 = words[i-1]
            word2 = words[i]
            l = min(len(word1),len(word2))
            for index in range(0,l):
                if word1[index] != word2[index]:
                    g[word1[index]].append(word2[index])
                    if word1[index] in g[word2[index]]:
                        return ""
                else:
                    self.visited[ord(word1[index])-ord('a')] = False
                    g[word1[index]].append(word1[index])
       
        for word in words:
            for ch in word:
                #print "checking %s" % ch
                if self.visited[ord(ch)-ord('a')] == False:
                    self.graphutil(g,stack,ch)
        stack.reverse()
        if not len(stack):
            return (words[0][0],"")[len(words) == 0]
        return ''.join(stack)
