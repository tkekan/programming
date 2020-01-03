import heapq
def frequencySort(s):
    """
    :type s: str
    :rtype: str
    """
    d = dict()
    for l in s:
        d[l] = d.get(l,0) + 1
        
    h = []
    for key,values in d.items():
        heapq.heappush(h,(-values,key))
    out = ""
    while len(h):
        t = heapq.heappop(h)
        out += str((t[0] * -1) * t[1])
    print out
s = "ababc"
frequencySort(s)
