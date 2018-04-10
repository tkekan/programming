class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

def splitListToParts( root, k):
    # Count the length of the linked list
    curr, length = root, 0
    while curr:
        curr, length = curr.next, length + 1
    # Determine the length of each chunk
    chunk_size, longer_chunks = length // k, length % k
    res = [chunk_size + 1] * longer_chunks + [chunk_size] * (k - longer_chunks)
    # Split up the list
    prev, curr = None, root
    for index, num in enumerate(res):
        if prev:
            prev.next = None
        res[index] = curr
        for i in range(num):
            prev, curr = curr, curr.next
    return res

root = Node(1)
root.next = Node(2)
root.next.next = Node(3)
root.next.next.next = Node(4)
root.next.next.next.next = Node(5)
root.next.next.next.next.next = Node(6)
root.next.next.next.next.next.next = Node(7)
root.next.next.next.next.next.next.next = Node(8)
res = splitListToParts(root,5)
for items in res:
    print "\n"
    while items:
        print str(items.data) + "-",
        items = items.next
