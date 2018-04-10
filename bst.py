


class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def findABC(root, target, ans):
    if root == None:
        return "Not Found"

    if root.data == target:
        if len(ans) > 0:
            return ans
        else:
            return "Undefined"

    if target > root.data:
        ans = findABC(root.right, target, ans + "1")
        return ans
    elif target < root.data:
        ans = findABC(root.left, target, ans + "0")
        return ans

    


root = Node(5)
root.left = Node(2)
root.right = Node(8)
root.left.left = Node(1)
root.left.right = Node(3)
root.right.left = Node(6)
root.right.right = Node(9)

ans = ""
num = 10
ans =  findABC(root, num, ans)
print ans,
