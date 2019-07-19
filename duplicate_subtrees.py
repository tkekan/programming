from collections import defaultdict
dic = defaultdict(list)
dic2 = defaultdict(int)
result = set()
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None



def helper(root):
    if root == None:
        return '#'

    path = str(root.val) + helper(root.left) + helper(root.right)

    if dic[path] == 1:
        result.append(root)

    dic[path] += 1

    return path

def findDuplicateSubtrees(root):
    """
    :type root: TreeNode
    :rtype: List[TreeNode]
    """
    if root == None:
        return None,[]
    
    left,lchild = findDuplicateSubtrees(root.left)
    right,rchild = findDuplicateSubtrees(root.right)
    
    if root.val in dic:
        check_child = [root.val]
        if left:
            check_child.append(left.val)
            [check_child.append(x) for x in lchild]
        if right:
            check_child.append(right.val)
            [check_child.append(x) for x in rchild]
        if dic[root.val] == check_child:
            tup = tuple(check_child)
            result.add(tup)      
    else:
        dic[root.val].append(root.val) 
        if left:
            dic[root.val].append(left.val)
            [dic[root.val].append(x) for x in lchild]
        if right:
            dic[root.val].append(right.val)
            [dic[root.val].append(x) for x in rchild]
    return root,dic[root.val]

root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(4)
root.right = TreeNode(3)
root.right.right = TreeNode(4)
root.right.left = TreeNode(2)
root.right.left.left = TreeNode(4)

findDuplicateSubtrees(root)
print result

