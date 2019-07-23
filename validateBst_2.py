import sys


class Node(object):
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

def bstutil(root, minv, maxv):
    if root == None:
        return True

    if root.val < minv or root.val > maxv:
        return False

    return bstutil(root.left, minv, root.val - 1) and \
           bstutil(root.right, root.val + 1, maxv)


def isValid(root):
    return bstutil(root, -(sys.maxint-1), sys.maxint)


root = Node(3)
root.left = Node(2)
root.right = Node(5)
root.left.left= Node(1)
root.left.right = Node(4)

print isValid(root)
