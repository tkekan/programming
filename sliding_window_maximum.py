def maxSlidingWindow(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: List[int]
    """
    dic = dict()
    if len(nums) < k:
        return 0
    maxsum = 0
    totalsum = 0
    q = []
    result = []
    for index in range(0,len(nums)):
        if len(q) != 0 and q[0] == index - k:
            q.pop(0)
            
        while len(q) and nums[q[-1]] < nums[index]:
            q.pop()
            
        q.append(index)
        if index >= k -1:
            result.append(nums[q[0]])
    return result

num = [1,3,-1,-3,5,3,6,7]
k = 3
print maxSlidingWindow(num, k)
