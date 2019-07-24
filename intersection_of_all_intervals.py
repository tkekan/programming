


def intersection(intervals):

    if len(intervals) == 1:
        return intervals[0]

    prev = intervals[0]
    for index in range(1, len(intervals)):
        if intervals[index][0] > prev[1]:
            return [-1,-1]
        else:
            left = intervals[index][0]
            right = min(prev[1], intervals[index][1])
            prev = [left, right]
    print prev

    


intervals = [[1, 6], [2, 8], [3, 10], [5, 8]]
intersection(intervals)
