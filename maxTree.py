
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def util(nums, low, high):
    if ( high < low or low < 0  or low == high ) :
        return None
    
    maxVal = max(nums[low:high])
    maxId = nums.index(maxVal)
    root = TreeNode(maxVal)
    #if maxId > prevId:
    #    low = prevId + 1
    root.left = util(nums, low, maxId )
    root.right = util(nums, maxId + 1, high)
    return root


def inorder(root):
    if root == None:
        return
    inorder(root.left)
    print " %d" % root.val,
    inorder(root.right)

def constructMaximumBinaryTree(nums):
    """
    :type nums: List[int]
    :rtype: TreeNode
    """
    root = util(nums, 0, len(nums))
    return root

nums = [3,2,1,6,0,5]
root = constructMaximumBinaryTree(nums)
print inorder(root)

