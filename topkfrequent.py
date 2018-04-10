

def topKFrequent(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: List[int]
    """
    sorted(nums)
    d = {}
    for items in nums:
        if items not in d.keys():
            d[items] = 1
            continue
        d[items] = d[items] + 1
    ans = sorted(d.items(), key = lambda x: x[1], reverse = True)
    results = map(lambda x: x[0], ans) 
    print results[0:k]

nums = [4,1,-1,2,-1,2,3]
topKFrequent(nums, 2)
