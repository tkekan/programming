class Node:
    def __init__(self,val):
        self.val = val
        self.next = None



def ispali(root):
    count = 0
    if root == None or root.next == None:
        return True

    temp = root
    while temp:
        temp = temp.next
        count += 1

    prev = root
    curr = root.next
    for index in range(1, count / 2):
        nextn = curr.next
        curr.next = prev
        prev = curr
        curr = nextn

    if count % 2 != 0:
        curr = curr.next
        

    pointer1 = prev
    pointer2 = curr

    for index in range(0, count / 2):
        if pointer1.val != pointer2.val:
            return False
        pointer1 = pointer1.next
        pointer2 = pointer2.next
    return True
# 1 - 2 - 1
# 1 - 2 - 2 - 1
root = Node(1)
root.next = Node(2)
root.next.next = Node(2)
root.next.next.next = Node(2)
print ispali(root)
