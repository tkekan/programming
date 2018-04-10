

def abc(m):
    m += 10
    print 'abc %d' % m

m = 10
print 'outside %d' % m
abc(m)
print 'outside %d' % m
