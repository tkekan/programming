import heapq
def smallestRange(nums):
    """
    :type nums: List[List[int]]
    :rtype: List[int]
    """
    
    if nums == None or len(nums) == 0:
        return []
    k = len(nums)
            
    max_num = float('-inf')
    hq = []
    for i in range(k):
        if nums[i][0] > max_num:
            max_num = nums[i][0]
        heapq.heappush(hq, [ nums[i][0], i, 0])
    min_len = float('inf')
    res = []
    while 1:
        num, list_index, elem_idx = heapq.heappop(hq)
        if max_num - num < min_len:
            res = [num , max_num]
            min_len = max_num - num
        elif max_num - num == min_len:
            if num < res[0]:
                res = [num,max_num]
        if elem_idx +1 == len(nums[list_index]):
            break
        heapq.heappush(hq, [nums[list_index][elem_idx+1] , list_index, elem_idx+1])
        if nums[list_index][elem_idx+1] > max_num:
            max_num = nums[list_index][elem_idx+1]
    return res

nums = [[4,10,15,24,26], [0,9,12,20], [5,18,22,30]]
smallestRange(nums)
