


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
    print quo


divide(100,30)
