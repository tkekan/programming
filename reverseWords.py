


def reverser(s):
    size = len(s)
    l = 0
    counter = 0
    d = list(s)
    r = -1
    while counter < size:
        while d[counter].isalpha():
            counter+=1
            if counter == size:
                break
        r = counter - 1
        while l < r:
            d[l], d[r] = d[r], d[l]
            l+=1
            r-=1
        if counter == size :
            break
        while not d[counter].isalpha():
            counter+=1
        l = counter
    print ''.join(d)

def reverse(s):
	l = 0;
	s = list(s)
	r = len(s) - 1;
	while l <= r:
		s[l] , s[r] = s[r], s[l]
		l += 1
		r -= 1
	return ''.join(s) 


s = "the sky is blue"
s = reverse(s)
reverser(s)
