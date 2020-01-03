class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwo(self,l1,l2):
        if not l1:
            return l2
        if not l2:
            return l1
        
        if l1.val < l2.val:
            result = l1
            result.next = self.mergeTwo(l1.next,l2)
        else:
            result = l2
            result.next = self.mergeTwo(l1, l2.next)
        return result
    
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if not lists:
            return None
        
        start = 0
        end = len(lists) - 1
        while start < end:
            s = start
            e = end
            while s < e:
                lists[s] = self.mergeTwo(lists[s], lists[e])
                s += 1
                e -= 1
                if s >= e:
                    end = e
                    break
        return lists[0]

    def displayMerged(self, l):
        while l:
            print l.val,
            l = l.next

node1 = ListNode(1)
node1.next = ListNode(4)
node1.next.next = ListNode(5)

node2 = ListNode(1)
node2.next = ListNode(3)
node2.next.next = ListNode(4)

node3 = ListNode(2)
node3.next = ListNode(6)

s = Solution()
l = [node1,node2,node3]
newList = s.mergeKLists(l)
s.displayMerged(newList)
