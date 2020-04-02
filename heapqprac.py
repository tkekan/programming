
import heapq



class Node:
    def __init__(self, val, name):
        self.val = val
        self.name = name


    def __lt__(self, other):
        return self.val < other.val

    def __str__(self):
        return str("{} : {}".format(self.val, self.name))
 
d = dict()

N1 = Node(100,"a")
N2 = Node(10, "b")
N3 = Node(30, "c")   
d['a'] = N1
items = [N1, N2, N3]

h = []
for item in items:
    heapq.heappush(h,item)

node = d['a']
node.val = -10
heapq.heapify(h)

while len(h):
    print (heapq.heappop(h))


