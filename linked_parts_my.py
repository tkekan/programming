
class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


def splitListToParts(root, k):
    """
    :type root: ListNode
    :type k: int
    :rtype: List[ListNode]
    """
    head = root
    length = 0
    while head:
        length+=1
        head = head.next
        
    chunk = length / k
    left = length % k
    results = []
    head = root
    while head:
        size = chunk
        if left > 0:
            size = chunk + 1
            left -= 1
        tmp  = head
        temp = []
        prev = None
        while size > 0:
            temp.append(tmp.data)
            if prev:
                prev.next = tmp
            prev = tmp
            tmp = tmp.next
            size -= 1
        prev.next = None
        results.append(temp)
        head = tmp
    while len(results) < k:
        results.append([])
    return results

root = Node(1)
root.next = Node(2)
root.next.next = Node(3)
root.next.next.next = Node(4)

root.next.next.next.next = Node(5)
root.next.next.next.next.next = Node(6)
root.next.next.next.next.next.next = Node(7)
'''
root.next.next.next.next.next.next.next = Node(8)
'''
res = splitListToParts(root, 3)
print res
