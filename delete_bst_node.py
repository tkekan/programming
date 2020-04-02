

class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

def sucessor(root):
    temp = root.right
    while temp and temp.left:
        temp = temp.left
    return temp.val

def util(root,key):
    if root == None:
        return None
    if root.val < key:
        root.right = util(root.right,key)
    elif root.val > key:
        root.left = util(root.left,key)
        
    else:
        if root.left == None:
            temp = root.right
            root = None
            return temp
        elif root.right == None:
            temp = root.left
            root = None
            return temp
        else:
            temp = sucessor(root)
            root.val = temp
            root.right = util(root.right,temp)
    return root


def preorder(root):
    if root == None:
        return
    preorder(root.left)
    print root.val, 
    preorder(root.right)

root = Node(5)
root.left = Node(3)
root.left.left = Node(2)
root.left.right = Node(4)
root.right = Node(6)
root.right.right = Node(7)

temp = util(root,3)
preorder(temp)
