
import heapq
def minmeeting(intervals):
    rooms = 0
    h = []
    intervals = sorted(intervals)
    for index in range(0,len(intervals)):
        if len(h) == 0:
            heapq.heappush(h,intervals[index][1])
            rooms += 1
        else:
            if h[0] <= intervals[index][0]:
                heapq.heappop(h)
                heapq.heappush(h, intervals[index][1])
            else:
                heapq.heappush(h,intervals[index][1])
                rooms += 1
    return rooms


intervals = [[0,30],[5,10],[15,20]]
intervals = [[2,15],[36,45],[9,29], [16,23], [4,9]]
print minmeeting(intervals)
        
