
import math

def generatesub(sub):
    l  = len(sub)
    result = []
    mr = []
    possible = math.pow(2,l)
    for count in range(0,l + 1):
        mr = []
        for size in range(0,l):
            if count == 0:
                result.append(mr)
                break;
            mr = sub[size:size + count]
            if len(mr) == count:
                result.append(mr)

    print result
        

def generatesub_recursive(s):
   

s = [1,2,3,4]
generatesub(s)
generatesub_recursive(s)
