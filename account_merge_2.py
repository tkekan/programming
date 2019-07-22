from collections import defaultdict
class Solution(object):
    
    def dfs(self, temp, values, visited, accounts):
        idx = values.pop(0)
        visited[idx] = True
        for emails in accounts[idx][1:]:
            temp.add(emails)
        if len(values) and visited[values[0]] == False:
            self.dfs(temp, values, visited, accounts)
        
    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """
        results = []
        dic = defaultdict(list)
        for index in range(0,len(accounts)):
            for email in accounts[index][1:]:
                dic[email].append(index)
        
        visited = [False] * len(accounts)
        for keys,values in dic.items():
            temp = set()
            temp.add(keys)
            name = accounts[values[0]][0]
            if visited[values[0]] == False:
                self.dfs(temp,values, visited, accounts)
                results.append([name] +list(temp))
                    
        print results


s = Solution()
accounts = [["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
accounts = [["Alex","Alex5@m.co","Alex4@m.co","Alex0@m.co"],["Ethan","Ethan3@m.co","Ethan3@m.co","Ethan0@m.co"],["Kevin","Kevin4@m.co","Kevin2@m.co","Kevin2@m.co"],["Gabe","Gabe0@m.co","Gabe3@m.co","Gabe2@m.co"],["Gabe","Gabe3@m.co","Gabe4@m.co","Gabe2@m.co"]]
s.accountsMerge(accounts)
