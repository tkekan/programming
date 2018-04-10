import math


def convert(s):
    pars = s.split('e')
    first = pars[0]
    second = pars[-1]
    exp = 1
    sum = 0.0
    divide = 1
    for i in range(len(first) - 1,-1,-1):
        if first[i] == '.':
            divide = exp
            continue
        sum = sum + exp * (ord(first[i]) - 48)
        exp = exp * 10
    sum = sum / divide
    divide = int(second)
    value = math.pow(10, divide)
    print value
    sum = float(sum * value)
    return sum

s = "2.23e-5"
num = convert(s)
print "%f " %num

