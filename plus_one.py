
def plusone(last):
    if not num:
        return []
    carry = 1
    for index in range(len(num)-1, -1, -1):
        sumv = last[index] + carry
        last[index] = sumv % 10
        carry = sumv / 10
        if carry < 1:
            break
    if carry > 0:
        return [1] + num
    else:
        return num
        

num = [9,9,9]
print plusone(num)
