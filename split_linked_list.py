
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def splitListToParts(self, root, k):
        """
        :type root: ListNode
        :type k: int
        :rtype: List[ListNode]
        """
        
        temp = root
        count = 0
        result = [[] for x in range(0,k)]
        while temp:
            count += 1
            temp = temp.next
        l = count / k
        remainder = 0
        if count > k:
            remainder = count % k 
        for index in range(0,k):
            templ = l
            if templ == 0 and root:
                result[index].append(root)
                root = root.next
            else:
                while templ > 0 and root:
                    res = []
                    result[index].append(root)
                    templ -= 1
                    root = root.next
            if remainder > 0:
                if root:
                    result[index].append(root)
                    root = root.next
                    remainder -= 1
        return result

root = ListNode(1)
root.next = ListNode(2)
root.next.next = ListNode(3)
root.next.next.next = ListNode(4)
s = Solution()
l =  s.splitListToParts(root, 5)
print l
for index in range(0,len(l)):
    for items in l[index]:
        print items.val,
