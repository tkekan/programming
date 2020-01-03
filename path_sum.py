# Definition for a binary tree node.
class Node(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def util(self,root,total):
        if root == None:
            return False
        
        self.t.append(root.val)
        if root.left == None and root.right == None \
            and root.val == total:
            l = list(self.t)

            self.ans.append(l)
            return True
        
        
        left = self.util(root.left,total-root.val)
        if left: 
            self.t.pop()
        right = self.util(root.right,total-root.val)
        if right:
            self.t.pop()
        return True
        
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        self.t = []
        self.ans = []
        self.util(root,sum)
        return self.ans

root = Node(5)
root.left = Node(4)
root.left.left = Node(11)
root.left.left.left = Node(7)
root.left.left.right = Node(2)
root.right = Node(8)
root.right.left = Node(13)
root.right.right = Node(4)
root.right.right.left = Node(5)
root.right.right.right = Node(1)
s = Solution()
print s.pathSum(root,22)

