import math


def factors(num):
    if num == 0:
        return []
    result = []
    for f in range(1, int(math.sqrt(num)) + 1):
        if num % f == 0:
            result.append(f)

    print result

factors(120)
