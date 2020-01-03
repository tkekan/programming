

class Node():
    def __init__(self,val):
        self.val = val
        self.next = None


def reverse(head):
    if not head.next:
        return None

    else:
        root = reverse(head.next)
        if not root:
            root = head.next
        head.next.next = head
        head.next = None
    return root

root = Node(1)
root.next = Node(2)
root.next.next = Node(3)
root.next.next.next = Node(4)
root.next.next.next.next = Node(5)

root = reverse(root)
temp = root
while temp:
    print temp.val,
    temp = temp.next

