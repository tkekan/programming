

def totaltime(tasks, k):
    tdic = {}
    time = 0
    start = 0
    for index in range(0, len(tasks)):
        '''if index - start >= k + 1:
            if index - tdic[tasks[start]] >= k + 1:
                del tdic[tasks[start]]
                start += 1'''
        if tasks[index] not in tdic:
            tdic[tasks[index]] = time
            time += 1
            continue
        else:
            previdx = tdic[tasks[index]]
            if time - previdx <= k:
                time = time + ( k + 1) - (time - previdx)
                tdic[tasks[index]] = time
            else:
                tdic[tasks[index]] = time
            time += 1
    print time		
    return time




tasks = [1,2,1,1,2,2,2,1,2,1,1,1]
#tasks = [1,2,1]
time = totaltime(tasks, 2)
assert time == 24
