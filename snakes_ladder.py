


def get(s, N):
        
        quot = (s-1)/N
        rem =  (s-1)%N
        
        r = N-1-quot
        c = rem if r%2 != N%2 else N - 1 - rem
        return r,c


print get(2,3);


