from collections import defaultdict
class Solution(object):
    
    def dfs(self, temp, values, visited, accounts, dic):
        idx = values.pop(0)
        if visited[idx] == True:
            return
        visited[idx] = True
        idx_set = set()
        for emails in accounts[idx][1:]:
            temp.add(emails)
            for ids in dic[emails]:
                if visited[ids] == False:
                    idx_set.add(ids)
        [values.append(x) for x in idx_set]
        while len(values): 
            self.dfs(temp, values, visited, accounts, dic)
        
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
                self.dfs(temp,values, visited, accounts, dic)
                results.append([name] +sorted(list(temp)))
                    
        print results


s = Solution()
#PASS
accounts = [["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
#PAss
accounts = [["Alex","Alex5@m.co","Alex4@m.co","Alex0@m.co"],["Ethan","Ethan3@m.co","Ethan3@m.co","Ethan0@m.co"],["Kevin","Kevin4@m.co","Kevin2@m.co","Kevin2@m.co"],["Gabe","Gabe0@m.co","Gabe3@m.co","Gabe2@m.co"],["Gabe","Gabe3@m.co","Gabe4@m.co","Gabe2@m.co"]]
#FAIL
accounts = [["David","David0@m.co","David4@m.co","David3@m.co"],["David","David5@m.co","David5@m.co","David0@m.co"],["David","David1@m.co","David4@m.co","David0@m.co"],["David","David0@m.co","David1@m.co","David3@m.co"],["David","David4@m.co","David1@m.co","David3@m.co"]]
s.accountsMerge(accounts)
