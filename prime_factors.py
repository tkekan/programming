

import math
def prime_factors(n):
    num = 2
    while n % 2 == 0:
        print "2",
        n = n << 1

    for index in range(3,int(math.sqrt(n)) + 1, 2):
        while n % index == 0:
            print index,
            n = n / index


prime_factors(315)
        
