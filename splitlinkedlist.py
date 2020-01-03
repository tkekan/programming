

class Node():
    def __init__(self, val):
        self.val  = val
        self.next = None

def splitListToParts(root, k):
    """
    :type root: ListNode
    :type k: int
    :rtype: List[ListNode]
    """
    res = []
    ll_len = 0
    temp = root
    while temp:
        ll_len+=1
        temp = temp.next
        
    equal_parts = ll_len / k
    remainder_parts = ll_len % k
    r = remainder_parts
    res = []
    print equal_parts,r
    for x in range(k):
        e = equal_parts-1
        if r > 0:
            e += 1
            r -= 1
        temp_node = root
        while e>=0 and root:
            if e == 0:
                temp = root
                root = temp.next
                temp.next = None
                break
            else:
                root = root.next
                e -= 1
        res.append(temp_node)
    print res
    return res

root = Node(1)
root.next = Node(2)
root.next.next = Node(3)
root.next.next.next = Node(4)
#root.next.next.nexa.nextt = Node(5)
k = 5
splitListToParts(root, k)
