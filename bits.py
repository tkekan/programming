

def func():
    num = 15
    bits = 0
    temp = num
    while True:
        temp = temp & (0x1 << bits)
        if temp == 0:
            break
        else:
            temp = num
            bits = bits + 1
    print bits


func()
