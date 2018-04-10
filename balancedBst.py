class Tree():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    




def height(root):
    if root == None:
        return 0

    return 1 + max( height(root.left), height(root.right))

def isBalance(root):
    if root == None:
        return False
    
    left = height(root.left)
    right = height(root.right)
    return abs(left - right) <= 1


def inorder(root, nums):
    if root == None:
        return
    
    inorder(root.left, nums)
    nums.append(root.data)
    inorder(root.right, nums)



def balanceutil(root, left, right, nums):
    if right < left or left > right:
        return None

    mid = left + (( right - left ) / 2)    
    root = Tree(nums[mid])
    root.left = balanceutil(root, left, mid - 1, nums)
    root.right = balanceutil(root, mid + 1, right, nums)
    
    return root

def balance(root):
    nums = []
    inorder(root, nums)
    left = 0
    right = len(nums) - 1
    
    root = balanceutil(root, left, right, nums)
    print "After balancing : ",
    print root.data
    print root.left.data
    print root.right.data


root = Tree(3)
root.left = Tree(2)
root.left.left = Tree(1)
'''
root = Tree(10)
root.left = Tree(8)
root.left.left = Tree(4)
root.left.right = Tree(9)
root.right = Tree(15)
root.right.left = Tree(12)
root.right.right = Tree(20)
root.right.right.right = Tree(30)
root.right.right.right.right = Tree(40)
'''

print isBalance(root)
nums = []
balance(root)

