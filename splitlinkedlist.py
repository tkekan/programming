

class Node():
    def __init__(self, val):
        self.val  = val
        seflf.next = None



root = Node(1)
root.next = Node(2)
root.next.next = Node(3)
root.next.next.next = Node(4)
root.next.next.nexa.nextt = Node(5)
k = 2
splitlist(root, k)
