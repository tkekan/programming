# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:
    def __init__(self):
        self.string = []
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if root == None:
            self.string.append(-1)
            return self.string
        self.string.append(root.val)
        self.string = self.serialize(root.left)
        self.string = self.serialize(root.right)
        return self.string
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if len(data):
            val = data[0]
            data.pop(0)
            if val == -1:
                return None
            root = TreeNode(val)
            root.left = self.deserialize(data)
            root.right = self.deserialize(data)
            return root

    def preorder(self, root):
        if root == None:
            return
        print root.val,
        self.preorder(root.left)
        self.preorder(root.right)
        
        

# Your Codec object will be instantiated and called as such:
codec = Codec()
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.right.left = TreeNode(4)
root.right.right = TreeNode(5)
path = codec.serialize(root)
print path
root = codec.deserialize(path)
codec.preorder(root)
