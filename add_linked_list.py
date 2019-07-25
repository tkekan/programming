class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def __init__(self):
        pass

    def add(self, l1, l2):
        if l1 == None or l2 == None:
            return 0
        
        carry = self.add(l1.next,l2.next)
        sumv = l1.val + l2.val + carry
        carry = sumv / 10
        node = ListNode(sumv%10)
        node.next = self.head
        self.head = node
        return carry
        
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        tl1 = l1
        l1len = 0
        while tl1:
            l1len += 1
            tl1 = tl1.next
            
        tl2 = l2
        l2len = 0
        while tl2:
            l2len += 1
            tl2 = tl2.next
            
        if l1len > l2len:
            for index in range(0, l1len-l2len):
                temp = ListNode(0)
                temp.next = l2
                l2 = temp
        elif l2len > l1len:
            for index in range(0, l2len - l1len):
                temp = ListNode(0)
                temp.next = l1
                l1 = temp
        self.head = None       
        self.add(l1,l2)
        return self.head

first = ListNode(7)
first.next = ListNode(2)
first.next.next = ListNode(4)
first.next.next.next = ListNode(3)

second = ListNode(5)
second.next = ListNode(6)
second.next.next = ListNode(4)
s = Solution()
slist = s.addTwoNumbers(first,second)

while slist:
    print slist.val,
    slist = slist.next
