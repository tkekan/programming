from collections import defaultdict
class Solution:    
    def criticalConnections(self,n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: List[List[int]]
        """
        degree = [0] * n
        d = defaultdict(list)
        for e in connections:
            d[e[0]].append(e[1])
            d[e[1]].append(e[0])
        visited = [-1] * n
        low = [-1] * n
        self.time = 0
        ans = []
        
        def dfs(curr, parent):
            self.time += 1
            visited[curr] = self.time
            low[curr] = visited[curr]
            for nei in d[curr]:
                if visited[nei] == -1:
                    dfs(nei,curr)
                    low[curr] = min(low[curr],low[nei])
                    if low[nei] > visited[curr]:
                        ans.append([curr,nei])
                elif nei != parent:
                    low[curr] = min(low[curr],visited[nei])
         
        dfs(0,0)
        return ans

s = Solution()
n = 4
e = [[0,1],[1,2],[2,0],[1,3]]
print s.criticalConnections(n,e)
