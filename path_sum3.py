# Definition for a binary tree node.
class Node(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def util(self,root,total,tdic,currsum):
        if root == None:
            return

        currsum += root.val
        if currsum == total:
            self.count += 1
        if (currsum - total) in tdic.keys():
            self.count += tdic[currsum-total]
        tdic[currsum] = 1
        self.util(root.left,total,tdic,currsum)
        self.util(root.right,total,tdic,currsum)
        
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        self.count = 0
        tdic = {0:0}
        self.util(root,sum,tdic,0)
        return self.count


root = Node(10)
root.left = Node(5)
root.left.left = Node(3)
root.left.left.left = Node(3)
root.left.left.right = Node(-2)
root.left.right = Node(2)
root.left.right.right = Node(1)
root.right = Node(-3)
root.right.right = Node(11)
root2 = Node(1)
root2.left = Node(-2)
root2.right = Node(-3)
s = Solution()
print s.pathSum(root2,-1)
