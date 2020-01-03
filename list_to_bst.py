# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def util(self, head, count):
        if count == 0:
            return None,head
        
        left,head = self.util(head,count/2)
        root = TreeNode(head.val)
        root.left = left
        head = head.next
        root.right,head = self.util(head,count - count/ 2 - 1)
        return root,head
        
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        count = 0
        temp = head
        if not head:
            return head
        
        while temp:
            count += 1
            temp = temp.next
        return self.util(head, count)

#[-10,-3,0,5,9]
head = ListNode(-10)
head.next = ListNode(-3)
head.next.next = ListNode(0)
head.next.next.next = ListNode(5)
head.next.next.next.next = ListNode(9)

s = Solution()
root,ignore = s.sortedListToBST(head)
print root,root.val
