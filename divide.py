


def findones(bits):
    count = 0
    while bits != 0:
        if bits & 0x1 == 0x1:
            count += 1
        bits = bits >> 1
    return count

def divide(num, divi):
    bits = 0
    original = num
    while num >= 0:
        sub = num - divi
        if sub < 0:
            break
        num = sub
        bits = (bits | 0x1) << 1
        
    quo  = findones(bits)
    print quo,num

def divide2(num,divi):
    res = 0
    while num >= divi:
        bits = 0
        while num >= (divi << bits):
            bits += 1
        res = res + (1 << (bits-1))
        num = num - (divi << (bits-1))
    print res,num

divide2(10,3)
num = 30
print num >> 30
