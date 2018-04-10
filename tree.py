from collections import deque
from collections import defaultdict

class Tree():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def levelorder(self,root,d):
        if root == None:
            return
        if d == 1:
            print " " + str(root.data),
        else:
            self.levelorder(root.left, d - 1)
            self.levelorder(root.right, d - 1)

    def levelorderQ(self, root):
        q = deque()
        q.append(root)
        while len(q) > 0:
            root = q.popleft()
            if root.left :
                q.append(root.left)            
            if root.right:
                q.append(root.right)
            print " %d " % root.data,
            
    def verticalOrder(self, root, dic, key):
        if root == None:
            return
        
        dic[key].append(root.data)
        self.verticalOrder(root.left, dic, key - 1)
        self.verticalOrder(root.right, dic, key + 1)
        
    def invert(self, root2):
        if root2 == None:
            return None

        root3 = Tree(root2.data)
        root3.left = self.invert(root2.right)
        root3.right = self.invert(root2.left)

        return root3


    def height(self, root):
        if root == None:
            return 0
        else:
            return 1 + max( self.height(root.left) , self.height(root.right))

def inorder(root):
    if root == None:
        return
    inorder(root.left)
    print " %d " % root.data,
    inorder(root.right)


def inorderit(root):
    stack = []
    while True:
        while root != None:
            stack.append(root)
            root = root.left

        if root == None:
            root = stack.pop()
            print root.data,
            root = root.right
        if len(stack) < 1 and root == None: 
            return

def preorder(root):
    if root == None:
        return
    print "  %d" % root.data,
    preorder(root.left)
    preorder(root.right)


def preorderit(root):
    stack = []
    while True:
        if root == None:
            root = stack.pop()
            
        if root.right != None:
            stack.append(root.right)
        
        print " %d" % root.data,
        root = root.left
        if len(stack) < 1 and root == None:
            break

def preorderh(root):
    stack = []
    while root or len(stack) > 0:
        if root:
            print root.data,
            if root.right:
                stack.append(root.right)
            root = root.left
            continue
        elif len(stack) > 0:
            root = stack[-1]
            stack = stack[:-1]
        else:
            root = None


def postorder(root):
    if root == None:
        return
    postorder(root.left)
    postorder(root.right)
    print " %d " % root.data,        


def sumpaths(root3, sum, temp):
    if root3 == None:
        return False
    
    temp.append(root3.data)
    if root3.left == None and root3.right == None:
        if root3.data == sum:
            paths.append(list(temp))
        return True
    else:    
        removeL = sumpaths( root3.left, sum - root3.data, temp)
        if removeL:
            temp.pop()
        removeR = sumpaths( root3.right, sum - root3.data, temp)
        if removeR:
            temp.pop()
        return removeL or removeR
    

def minDepth(root):
    if root == None:
        return False,0

    leafl,leftl = minDepth(root.left)
    leafr,rightl = minDepth(root.right)
    
    if root.left == None and root.right == None:
        return True, min(leftl, rightl) + 1
    else:
        return leafl or leafr,1 + max(leftl,rightl)    

def postorderit(root):
    pass
root = Tree(3)
root.left = Tree(9)
root.right = Tree(20)
root.right.left = Tree(15)
root.right.right = Tree(7)
root.right.left.left = Tree(10)
root.right.left.right = Tree(12)

root1 = Tree(1)
root1.left = Tree(2)
root1.right = Tree(3)
root1.left.left = Tree(4)
root1.left.right = Tree(5)
root1.right.left = Tree(6)
root1.right.left.right = Tree(8)
root1.right.right = Tree(7)
root1.right.right.right = Tree(9)


root2 = Tree(1)
root2.left = Tree(2)
root2.right = Tree(3)
root2.left.left = Tree(4)
root2.left.right = Tree(5)
root2.left.right.left = Tree(8)
root2.right.left = Tree(6)
root2.right.right = Tree(7)


height = root.height(root1)
d = deque()

#Level Order
print " Level Order: ",
for i in range(height + 1, 0, -1):
    root.levelorder(root, i)
#End Level Order
#levelorderQ
print ""
print "Level Order using Q: ",
root.levelorderQ(root)

#
print ""
print "Vertical Order : "
dic = defaultdict(list)
root1.verticalOrder(root1, dic, 0)
#endVertical Order

# Invert Tree
root3 = root2.invert(root2)
print "Inorder recursive: ",
inorder(root2)

print " "
print "In order iterative: ",
inorderit(root2)

#Preorder recursive
print " "
print " Preorder : ",
preorder(root2)

#preorder iterative
print " "
print " Preorder iterative : ",
preorderit(root2)
print "\n Preorder h: ",
preorderh(root2)

#postorder recursive
print " "
print "Postorder recursive: ",
postorder(root2)

#postorder iterative
print " "
print "Postorder iterative: ",
postorderit(root2)


root3 = Tree(5)
root3.left = Tree(4)
root3.right = Tree(8)
root3.left.left = Tree(11)
root3.left.left.left = Tree(7)
root3.left.left.right = Tree(2)
root3.right.left = Tree(13)
root3.right.right = Tree(4)
root3.right.right.left = Tree(5)
root3.right.right.right = Tree(1)
paths = []
sumpaths(root3,22, [])
print " "
print " Paths is : "
print paths



#Minimum Depth of Binary Tree
ret,depth = minDepth(root3)
print ""
print "minimum dept of root3: %d" % depth,
print ""




#Convert preorder traversal by using only right pointers

def preorderConvert(root):
    if root == None:
        return None

    left = preorderConvert(root.left)
    right = preorderConvert(root.right)
    
    if right == None and left == None:
        return root

    if left != None:
        temp = root.right
        root.right = left
        tr = root
        while tr.right:
            tr = tr.right
        tr.right = temp

    return root

root4 = Tree(10)
root4.left = Tree(8)
root4.right = Tree(2)
root4.left.left = Tree(3)
root4.left.right = Tree(5)


root4 = preorderConvert(root4)
print "\npreorder Convert: \n"
while root4:
    print str(root4.data) + "-",
    root4 = root4.right
