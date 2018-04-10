#Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    maxcount = 0
    count = 1
    prev = None
    def util(self, root, nodes):
        if root == None:
            return
        self.util(root.left, nodes)
        if self.prev != None:
            if self.prev == root.val:
                self.count += 1
            else:
                self.count = 1
        if self.count > self.maxcount:
            self.maxcount = self.count
            del nodes[:]  
            nodes.append(root.val)
        elif self.count == self.maxcount:
            nodes.append(root.val)
        self.prev = root.val
        self.util(root.right, nodes)
        
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root == None:
            return []
        nodes = []
        self.util(root, nodes)
        return nodes

root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(2)
s = Solution()
vals = s.findMode(root)
print vals

