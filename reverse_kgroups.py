class Node(object):
    def __init__(self,val):
        self.val = val
        self.next = None

def util(head, k):
    prev = None
    right = None
    node = head
    count = 0
    while count < k and node != None:
        right = node.next
        node.next = prev
        prev = node
        node = right
        count += 1
    if right != None:
        head.next = util(right,k)
    return prev

head = None
node = head

for i in range(1,6):
    if head == None:
        head = Node(i)
        root = head
    else:
        root.next = Node(i)
        root = root.next
        
def printl(newhead):
    node = newhead
    while node:
        print node.val,
        node = node.next
printl(head)
print "\n"
newhead = util(head, 3)
printl(newhead)
