
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    def printlist(self):
        while self:
            print str(self.data) + " ",
            self = self.next

def reverse(head):
    if head.next == None:
        return head
    else:
        newHead = reverse(head.next)
        head.next.next = head
        head.next = None
    return newHead

def InsertNth(head, data, position):
    if head == None:
        head = Node(data)
        return head
    
    counter = 0
    nextPtr = head
    while counter < position - 1:
        nextPtr = nextPtr.next
        counter+=1
    
    temp = nextPtr.next
    nextPtr.next = Node(data)
    nextPtr.next.next = temp
    return head

def printl(head):
    while head != None:
        print str(head.data) + " ",
        head = head.next

def getLen(head):
    counter = 0
    while head:
        counter += 1
        head = head.next
    return counter

def oddEvenList( head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    if not head or head.next:
        return head
    oddp = head
    evenp = oddp.next
    oddpit = oddp
    evenpit = evenp
    while evenpit and evenpit.next:
        oddpit.next = evenpit.next
        oddpit = oddpit.next
        evenpit.next = oddpit.next
        evenpit = evenpit.next
     
    oddpit.next = evenp
    return oddp

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
head.printlist()
newh = oddEvenList(head)
newh.printlist()

print " Odd even list\n:"
newH = oddEvenList(head)
newH.printlist()
'''
insertH = None
insertH  = InsertNth(insertH, 3, 0)
insertH  = InsertNth(insertH, 5, 1)
insertH  = InsertNth(insertH, 4, 2)
insertH  = InsertNth(insertH, 2, 3)
insertH  = InsertNth(insertH, 10, 1)
insertH  = InsertNth(insertH, 20, 0)

printl(insertH)
'''
