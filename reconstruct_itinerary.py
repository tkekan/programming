from collections import defaultdict

def stack_sol(dic):
    stack = ['JFK']
    result = []  
    while len(stack):
        key = stack[-1]
        if key in dic and len(dic[key]) > 0:
            dest = dic[key]
            stack.append(dest.pop(0))
        else:
            result.append(stack.pop())
    result.reverse()
    print result
    
def findItinerary(tickets):
    """
    :type tickets: List[List[str]]
    :rtype: List[str]
    """
    dic = defaultdict(list)
    dic2 = defaultdict(list)
    for items in tickets:
        dic[items[0]].append(items[1])
        dic2[items[0]].append(items[1])
        
    for k,v in dic.items():
        dic[k] = sorted(v)
        dic2[k] = sorted(v)

    stack_sol(dic2)
    key = 'JFK'
    result = [key]
    endd = None
    while True:
        dest = dic[key]
        if len(dest):
            val = dest[0]
            if val in dic.keys() and len(dic[val]) > 0:
                result.append(dest.pop(0))
                #dic[key] = dest
                key = result[-1]
            else:
                endd = val
                dest.pop(0)
        else:
            break
    result.append(endd)
    return result

tickets = [["EZE","TIA"],["EZE","HBA"],["AXA","TIA"],["JFK","AXA"],["ANU","JFK"],["ADL","ANU"],["TIA","AUA"],["ANU","AUA"],["ADL","EZE"],["ADL","EZE"],["EZE","ADL"],["AXA","EZE"],["AUA","AXA"],["JFK","AXA"],["AXA","AUA"],["AUA","ADL"],["ANU","EZE"],["TIA","ADL"],["EZE","ANU"],["AUA","ANU"]]
res = findItinerary(tickets)
print res
