


def sum(total,num,power):
    value = num ** power
    if value == total:
	return 1
    if value > total:
	return 0
    return sum(total,num+1,power) + sum(total - value, num + 1, power)


ways = sum(100,1,2)
print ways
