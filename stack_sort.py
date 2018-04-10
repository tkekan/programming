




def insertSorted( num, var, length):
    if length == 0 or num[-1] < var:
        num.append(var)
        return
    else:
        temp = num.pop()
        insertSorted(num, var, len(num))
        num.append(temp)
            


def sortStack(num, length):
    if length > 0:
        temp = num.pop()
        sortStack(num, len(num))
        insertSorted(num, temp, len(num))






num = [-3,14,18,-5,30]
print "before fn :", num
sortStack(num, len(num) )
print "after fn: ",  num  
