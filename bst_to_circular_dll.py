# Definition for a Node.
class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

main_head = None
class Solution(object):
    def util(self, root, head):
        if root == None:
            return None,head
        
        node,head = self.util(root.left, head)
        if head == None:
            self.main_head = root
            head = root
        else:
            root.left = head
            head.right = root
            head = root
            
        node,head = self.util(root.right, head)
        return node,head

    def treeToDoublyList(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        self.main_head = None
        node, head = self.util(root, None)
        if head:
            head.right = self.main_head
            self.main_head.left = head
        return self.main_head
    
    def printList(self, head):
        temp = head
        while temp:
            print temp.val,
            temp = temp.right
            if temp == head:
                break


s =  Solution()
root = Node(4)
root.left = Node(2)
root.left.left = Node(1)
root.left.right = Node(3)
root.right = Node(5)
headlist = s.treeToDoublyList(root)
s.printList(headlist)
