


class Node():
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None


def CountNodes(root):
    h = height(root)
    if h < 0:
        return 0

    if height(root.right) == h-1:
        return ((1 << h) + CountNodes(root.right))
    else:
        return ((1 << h-1) + CountNodes(root.left))



def height(root):
    if root:
        return (1 + height(root.left))
    else:
        return int(-1)

def simplecount(root):
    if root == None:
       return
    simplecount.counter += 1
    simplecount(root.left)
    simplecount(root.right)

root = Node(1)
root.left = Node(2)
root.left.right = Node(3)
root.left.left = Node(4)
root.left.left.left = Node(5)
root.left.left.right = Node(11)
root.left.right.left = Node(6)
root.left.right.right = Node(7)
root.right = Node(8)
root.right.left = Node(9)
root.right.right = Node(10)
simplecount.counter = 0
simplecount(root)
print simplecount.counter
print CountNodes(root)

