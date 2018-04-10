class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None



def findBottomLeftValue( root):
    """
    :type root: TreeNode
    :rtype: int
    """
    a = []
    result = []
    a.append(root)
    while len(a) > 0:
        if a[0].right !=  None:
            a.append(a[0].right)
        if a[0].left != None:
            a.append(a[0].left)
        result = a[0]
        a = a[1:]
    return result.val

'''
def inOrderSucc(stack):
    while len(stack) > 0:
        node = stack[-1]
        stack = stack[0:-1]
        print str(node.val) + '->',
        if node.right != None:
            stack.append(node.right)
            node = node.right
            while node.left != None:
                node = node.left
                stack.append(node)
'''

def inorder(root):
    stack = []
    if root:
        stack.append(root)
    while len(stack) > 0:
        if root.left != None:
            root = root.left
            stack.append(root)
            continue
        node = stack[-1]
        stack = stack[:-1]
        print str(node.val) + '-',
        if node.right != None:
            stack.append(node.right)
            node = node.right
            root = node
            continue

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.right.left = Node(5)
root.right.right = Node(6)
root.right.left.left = Node(7)

val = findBottomLeftValue(root)
print val

print '\n'
print 'Inorder Traversal: ',
inorder(root)
