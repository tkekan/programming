from collections import defaultdict
import heapq
def leastInterval(tasks, n):
    """
    :type tasks: List[str]
    :type n: int
    :rtype: int
    """
    dic = defaultdict(int)
    for items in tasks:
        dic[items] += 1
        
    h = []
    for values in dic.values():
        heapq.heappush(h,(values * -1))
    cycles = 0  
    while len(h):
        temp = []
        for index in range(0,n+1):
            if len(h):
                temp.append(-1 * heapq.heappop(h))
        
        for items in temp:
            if items - 1 > 0:
                heapq.heappush(h,-1 * (items-1))
        cycles += (n+1, len(temp))[len(h) == 0]
    return cycles

tasks = ['A','A','A','B','B','B']
print leastInterval(tasks, 2)
