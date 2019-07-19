
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: Node
        :rtype: str
        """
        if root:
            q_ = [root]
            result = str(root.val) + ',#,'
        else:
            return '#'
        
        while len(q_):
            node = q_.pop(0)
            while len(node.children):
                temp = node.children.pop(0)
                q_.append(temp)
                result = result + str(temp.val) +','
            result = result + '#,'
       # print result[0:-1]
        return result[0:-1]

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: Node
        """
        l = data.split(',')
        if l[0] == '#':
            return None
        
        node = Node(l[0],[])
        rootNode = node
        q_ = [node]
        index = 1
        while len(q_):
            node = q_.pop(0)
            index += 1
            while index < len(l) and l[index] != '#':
                child = Node(l[index], [])
                node.children.append(child)
                q_.append(child)
                index += 1
        return rootNode

# Your Codec object will be instantiated and called as such:
 codec = Codec()
 codec.deserialize(codec.serialize(root))
