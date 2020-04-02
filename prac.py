
import sys
import heapq

def minimum(a, n):
    print sys.argv
    args = sys.argv
    n = int(args[1])
    a =  args[2:]
    h = []
  
    a = [items for items in set(a)]  
    
    for num in a:
        newvar = int(num)
        if len(h) < n:
            heapq.heappush(h, -newvar)
        else:
            if h[0] < -newvar:
                heapq.heappop(h)
                heapq.heappush(h,-newvar)
    
    print "Output: "
    while len(h):
        num =  heapq.heappop(h)
        print (num * -1),
        


a = [ 10, 20, 30, 40, 50, 5 ]
minimum(a, 2)
