

import sys
def func( num):
    if num == 4:
        print "2\n"
        return 2
    else: 
        return 2 * func ( num + 1)

sys.exit(func(2))

