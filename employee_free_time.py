
def merge(interval):
    mint = []
    for index in range(len(interval)):
        for items in interval[index]:
            mint.append(items)
    print mint
    mint.sort(key=lambda x: x[0])
    results = []
    for items in mint:
        if len(results) == 0 or results[-1][1] < items[0]:
            results.append(items)
        else:
            results[-1][1] = max(results[-1][1], items[1])
    ans = []
    for index in range(1,len(results)):
        first = results[index-1][1]
        second = results[index][0]
        ans.append([first,second])

    print ans



interval = [[[1,2],[5,6]],[[1,3]],[[4,10]]]
merge(interval)
