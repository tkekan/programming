


def binsearch(array, val):
    r = len(array) - 1
    l = 0
    while l <= r:
        mid = l + (r - l) / 2
        if array[mid] == val:
            return "found"
        if array[l] <= array[mid]:
            if val >= array[l] and array[mid] > val:
                r = mid - 1
            else:
                l = mid + 1
        elif array[mid] <= array[r]:
            if val > array[mid] and val <= array[r]:
                l = mid + 1
            else:
                r = mid - 1
    return "not found"




    """array[l] <= val and array[mid] > val:
            r = mid - 1
        else:
            l = mid + 1"""

array = [6,1,2,3,4,5]
res = binsearch(array, 1)
print res
