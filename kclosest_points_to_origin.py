import heapq
import math
def kClosest(points, K):
    """
    :type points: List[List[int]]
    :type K: int
    :rtype: List[List[int]]
    """
    h = []
    results = []
    for items in points:
        dist = pow(items[0],2)+pow(items[1],2)
        if len(h) < K:
            heapq.heappush(h, ((dist * -1),items))
        elif (dist * -1) < h[0]:
            heapq.heappop(h)
            heapq.heappush(h,((dist * -1),items))
    
    for items in h:
        results.append(items[1])
    print results
    return results

points = [[-95,76],[17,7],[-55,-58],[53,20],[-69,-8],[-57,87],[-2,-42],[-10,-87],[-36,-57],[97,-39],[97,49]]
K = 5
kClosest(points,K)
            
