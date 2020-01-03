


def check(num):
    low = 1
    high = num
    while low <= high:
        mid = (low + high) / 2
        value = mid * mid
        if value > num:
            high = mid - 1
        elif value == num:
            return mid
        else:
            low = mid + 1
    return -1



print check(65)
