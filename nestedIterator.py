class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.nested = nestedList

    def next(self):
        """
        :rtype: int
        """
        r = self.nested[0]
        if type(r) == list:
            if len(r) > 1:
                self.nested[0] = self.nested[0][1:]
            else:
                self.nested = self.nested[1:]
            return r[0]
        else:
            self.nested = self.nested[1:]
            return r

    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.nested) > 0
        

# Your NestedIterator object will be instantiated and called as such:
nestedList = [[1,1],2,[3,4]]
i, v = NestedIterator(nestedList), []
while i.hasNext(): v.append(i.next())
print v
