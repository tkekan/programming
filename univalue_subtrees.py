import sys

class Node():
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None


def count(root):
    global ans
    if root == None:
        return None

    left = count(root.left)
    right = count(root.right)
    if left and right and (left == right == root.val):
        count.counter += 1
    elif left and left == root.val:
        count.counter += 1
    elif right and right == root.val:
        count.counter += 1
    elif not left and not right:
        count.counter += 1

    ans = max(ans,count.counter)
    return root.val

def isUnivalue(root,val):
    if not root:
        return True
    if root.val != val:
        return False

    return isUnivalue(root.left,val) and isUnivalue(root.right, val)


root = Node(5)
root.left = Node(5)
root.right = Node(5)
root.left.left = Node(5)
root.left.right = Node(5)
root.right.right = Node(1)
ans = -sys.maxint
count.counter = 0
count(root)
print "IsUnivalue: %s" % ("True","False")[isUnivalue(root,root.val) == False]
