
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None




def merge_sorted(n1, n2):
    if not n1:
        return n2
    if not n2:
        return n1
    result = None
    if n1.data > n2.data:
       result = n2
       result.next = merge_sorted(n1, n2.next)
    elif n1.data < n2.data:
        result = n1
        result.next = merge_sorted(n1.next, n2)
    return result




def printlist(n):
    print "Inside printlist"
    while n:
        print n.data,
        n = n.next;

n1 = Node(1)
n1.next = Node(5)
n1.next.next = Node(20)

n2 = Node(4)
n2.next = Node(6)
n2.next.next = Node(30)
n2.next.next.next = Node(50)
n = merge_sorted(n1,n2)
printlist(n)
