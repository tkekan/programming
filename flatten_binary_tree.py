

def flatten(root):
    if not root:
        return

    while root:
        if root.left:
            node = root.left
            predes = node
            while predes.right:
                predes = predes.right
            rightNode = root.right
            root.right = node
            predes.right = rightNode
            root.left = None
        root = root.right
