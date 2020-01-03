


def printInterleaved(l1, l2, one):
    while len(l1) or len(l2):
        if one:
            if len(l1):
                result.append(l1.pop(0))
                one = False
                continue
            else:
                result.append(l2.pop(0))
        else:
            if len(l2):
                result.append(l2.pop(0))
                one = True
                continue
            else:
                result.append(l1.pop(0))
    



l1 = [1,2,3]
l2 = [4,5,6,7,8]
result = []
printInterleaved(l1,l2,True)
print result
