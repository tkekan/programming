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
        return maxsum

root = Node(5)
root.left = Node(4)
root.left.left = Node(11)
root.left.left.left = Node(7)
root.left.left.right = Node(2)
root.right = Node(8)
root.right.left = Node(13)
root.right.right = Node(4)
root.right.right.right = Node(1)
s = Solution()
s.maxPathSum(root)
print s.res
