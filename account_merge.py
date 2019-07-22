class accountC:
    def __init__(self, name, emails, dic):
        self.name = name
        self.emails = set()
        for items in emails:
            self.emails.add(items)
            dic[items] = self

class Solution(object):
    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """
        record = accounts[0]
        results = []
        email_r = []
        dic = dict()
        a1 = accountC(record[0], record[1:], dic)
        #for items in record[1:]:
        #    dic[items] = a1
        results.append(a1)
        for index in range(1,len(accounts)):
            record = accounts[index]
            account = None
            for items in record[1:]:
                if items in dic:
                    account = dic[items]
            if account!= None:
                for items in record[1:]:
                    dic[items] = account
                    account.emails.add(items)
            else:
                a1 = accountC(record[0], record[1:], dic)
                results.append(a1)

        for items in results:
            temp = []
            temp.append(items.name)
            temp = temp + sorted(list(items.emails))
            email_r.append(temp)
        return email_r

        

acc = [["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
s = Solution()
print s.accountsMerge(acc)
