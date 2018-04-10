
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None



def createList():
    Head = Node(1)
    main = Head
    for x in range(2,5):
        temp = Node(x)
        Head.next = temp
        Head = Head.next
    return main

def reorder():
    slow = Head
    fast = Head.next
    if fast == None or fast.next == None:
        return
    while  fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    head2 = slow.next
    slow.next = None

    current = None
    traverse = head2
    nxt = traverse
    while nxt:
        nxt = traverse.next
        traverse.next = current
        current = traverse
        traverse = nxt

    head2 = current
    ptr1 = Head
    ptr2 = head2
    nxt1 = ptr1
    nxt2 = ptr2
    newHead = ptr1
    while nxt1 and nxt2:
        nxt1= ptr1.next
        nxt2 = ptr2.next
        ptr1.next = ptr2
        ptr2.next = nxt1
        ptr1 = nxt1
        ptr2 = nxt2
    return Head
    
def printList(head):
    while head:
        print head.val,
        head = head.next


Head = createList()
printList(Head)
print "\n\n"
Head = reorder()
printList(Head)

