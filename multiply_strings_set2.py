

def multiply(num1, num2):
    result = [0] * (len(num1) + len(num2))
    r1 = 0
    for n1 in range(len(num1) - 1, -1 , -1):
        r2 = 0
        carry = 0
        total = 0
        for n2 in range(len(num2) - 1, -1 , -1):
            total = ((ord(num2[n2]) - ord('0')) * (ord(num1[n1]) - ord('0'))) + carry + result[r1+r2]
            result[r1+r2] = total % 10
            carry = total / 10
            r2 += 1
        if carry > 0:
            result[r1+r2] += carry
        r1 += 1
    result.reverse()
    print int(''.join(str(x) for x in result))


multiply("123","456")
