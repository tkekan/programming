import heapq
import math
def dist(x,y):
    return pow(x,2) + pow(y,2)

def partition(points, l, r, pivot)

def util(points, l, r, K):
    if l > r or l == r:
        return

    pivot = random.randint(l,r)
    pivot = partition(points, l, r, pivot)

    if pivot == K:
        return

    if k < pivot:
        return util(points, l, pivot-1, k)
    else:
        return util(points, pivot+1, r, k)

def kClosest(points, K):
    """
    :type points: List[List[int]]
    :type K: int
    :rtype: List[List[int]]
    """
    util(points,0,len(points)-1,K)

points = [[-95,76],[17,7],[-55,-58],[53,20],[-69,-8],[-57,87],[-2,-42],[-10,-87],[-36,-57],[97,-39],[97,49]]
K = 5
kClosest(points,K)
            
