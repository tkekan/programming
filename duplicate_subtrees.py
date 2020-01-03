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


def utils2(root,m):
    if not root:
        return ""
    ans = "("
    ans += utils2(root.left,m)
    ans += str(root.val)
    ans += utils2(root.right,m)
    ans += ")"

    if ans in m and m[ans] == 1:
        global res
        res.append(ans)
    else:
        m[ans] = 1

    return ans

nodeMap = defaultdict(list)
def outer(root):
    def helper2(root,nodeMap):
        if not root:
            return ''
        cur = str(root.val)
        ans = cur + 'l' + helper2(root.left, nodeMap) + \
                    'r' + helper2(root.right, nodeMap)
        nodeMap[ans].append(root.val)
        return ans
    helper2(root,nodeMap)
    ans = []
    for keys,nodes in nodeMap.items():
            if len(nodes) > 1:
                print keys,nodes[0]
    return ans

root = TreeNode(3)
root.left = TreeNode(2)
root.left.left = TreeNode(4)
root.right = TreeNode(3)
root.right.right = TreeNode(4)
root.right.left = TreeNode(2)
root.right.left.left = TreeNode(4)

findDuplicateSubtrees(root)
m = {}
res = []
utils2(root,m)
print res
print result
"""Outer is better than others """
print outer(root)
