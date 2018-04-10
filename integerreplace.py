def integerReplacement( n):
    """
    :type n: int
    :rtype: int
    """
    
    if n == 0:
        return 0
    
    if n % 2 == 0:
        integerReplacement( n << 1)
    else:
        integerReplacement( n - 1)

ways = integerReplacement(7)
print ways
