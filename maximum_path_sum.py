class Node(object):
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

class Solution(object):
    def __init__(self):
        self.res = -1
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        
        lsum = self.maxPathSum(root.left)
        rsum = self.maxPathSum(root.right)
        
        maxsum = max(max(lsum,rsum) + root.val, root.val)
        maxtop = max(maxsum, lsum +rsum + root.val)
        
        self.res = max(self.res, maxtop)
        return maxtop

root = Node(-10)
root.left = Node(9)
root.right = Node(20)
root.right.left = Node(15)
root.right.right = Node(7)
s = Solution()
s.maxPathSum(root)
print s.res
