


def findbits(n):
    count = 0
    while n != 1:
        if n % 2 == 0:
            n = n >> 1
        elif bin(n+1).count('1') < bin(n-1).count('1') and n != 3:
            n = n + 1
        else:
            n = n - 1
        count += 1
    print count
    
findbits(15)
