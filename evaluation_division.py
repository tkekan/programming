import collections
class Solution(object):
    
    def util(self, g, start, end, seen):
        if start not in g or end not in g:
            return (-1.0)
        
        if end in g[start]:
            return g[start][end]
        
        seen.add(start)
        for items in g[start]:
            if items not in seen:
                val = self.util(g, items, end, seen)
                if val != -1.0:
                    val = val * g[start][items]
                    return val
        return -1.0
                            
                
        
    
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        g = collections.defaultdict(lambda: collections.defaultdict(int))
        for e,v in zip(equations,values):
            g[e[0]][e[1]] = v
            g[e[1]][e[0]] = 1/v
            g[e[0]][e[0]] = 1.0
            g[e[1]][e[1]] = 1.0
            #g[e[0]]['seen'] = False
            #g[e[1]]['seen'] = False
        
        results = []
        for index in range(len(queries)):
            seen = set()
            result = self.util(g,queries[index][0], queries[index][1], seen)
            results.append(float(result))
        print results

s = Solution()
e = [["a","b"],["c","d"]]
v = [1.0,1.0]
q = [["a","c"],["b","d"],["b","a"],["d","c"]]
#e = [["x1","x2"],["x2","x3"],["x3","x4"],["x4","x5"]]
#v = [3.0,4.0,5.0,6.0]
#q = [["x1","x5"],["x5","x2"],["x2","x4"],["x2","x2"],["x2","x9"],["x9","x9"]]
#e = [ ["a", "b"], ["b", "c"] ]
#v = [2.0, 3.0]
#q = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ]
s.calcEquation(e, v, q)
