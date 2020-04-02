


def canjump(start, k, d, end):
    if start > end:
        return False
    if start == end:
        return True

    ret = False
    for index in range(k-1,k+2):
        if index <= 0:
            continue
        if start + index in d:
            ret = canjump(start + index,index,d,end)
            if ret == True:
                return True

    return ret
   

nums = [0,2]
d = {x:False for x in nums}
end = nums[-1]
print canjump(0, 0,d, end)
