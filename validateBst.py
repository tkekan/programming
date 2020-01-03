
class BST():
    def __init__(self, val):
       self.val = val 
       self.left = None
       self.right = None

def util( root, prev):
    if root == None:
        return prev, True
    
    prev, val =  util(root.left, prev)
    if not val:
        return prev, False
    if prev != None and prev.val >= root.val: 
        return prev, False
    prev = root
    prev, val = util(root.right, prev)
    return prev, val


def validateBST(root):
    prev = None
    prev, val = util(root, prev)
    print val

root = BST(5)
root.left = BST(1)
root.right = BST(4)
root.right.left = BST(3)
root.right.right = BST(7)

validateBST(root)
