import sys

def second(l):
    max = float('-inf')
    for item in l:
        if item > max:
            max = item

    first = l[0]
    second = 0
    for i in range(1,len(l)):
        if l[i] > first and l[i] < max:
            second = l[i]
            first = l[i]

    if second == 0:
        return first
    else:
        return second


s = second([5,6,1,4,4,1,2,3])
print s
