import sys

def create_min_stack(nums):
    stack = []
    minele = sys.maxint
    for items in nums:
        if len(stack) == 0:
            stack.append(items)
            minele = items
        else:
            if items < minele:
                stack.append(2 * items - minele)
                minele = items
            else: stack.append(items)
    return stack,minele

def create_max_stack(nums):
    stack = []
    maxele = -(sys.maxint -1)
    for items in nums:
        if len(stack) == 0:
            stack.append(items)
            maxele = items
        else:
            if items > maxele:
                stack.append(2 * items - maxele)
                maxele = items
            else: stack.append(items)
    return stack,maxele

def getminele(stack):
    if len(stack) and getminele.min != None:
        return getminele.min

def getmaxele(stack):
    if len(stack) and getmaxele.max != None:
        return getmaxele.max

def popstack(stack):
    print stack
    if len(stack):
        val = stack.pop()
        if val < getminele.min:
            getminele.min = (2 * getminele.min) - val
    print "after pop" , stack

    print "Minimum on stack is : %d" %getminele.min
        

def popmaxstack(stack):
    print stack
    if len(stack):
        val = stack.pop()
        if val > getmaxele.max:
            getmaxele.max = ( 2 * getmaxele.max) - val
    print "after pop" , stack

    print "Max on stack is : %d" %getmaxele.max

nums = [1, 100, 4, 20, 0, 40, -5, -3, 200]
print " putting into stack: ", nums
stack,minele = create_min_stack(nums)
getminele.min = minele
print getminele(stack)
popstack(stack)
print getminele(stack)
popstack(stack)
print getminele(stack)
popstack(stack)
print getminele(stack)
popstack(stack)
print getminele(stack)

stack,maxele = create_max_stack(nums)
getmaxele.max = maxele
print getmaxele(stack)
popmaxstack(stack)
