from pprint import pprint

def ismatch(s, p):
    isfirst = True
    wr = 0
    pa = list(p)
    print pa
    for i in range(0,len(pa)):
        if pa[i] == '*':
            if isfirst:
                pa[wr] = pa[i]
                isfirst = False
                wr+= 1
        else:
            pa[wr] = pa[i]
            wr += 1
            isfirst = True

    p = ''.join(pa[0:wr])		
    dp = [[False for x in range(len(p) + 1)] for y in range(len(s) + 1)]
    dp[0][0] = True

    for index in range(1,len(s)+1):
        print index, len(s)
        dp[index][0] = False

    if p[0] == '*':
        print "setting to true 0th entry"
        dp[0][1] = True

	#for index in range(1,len(p) + 1):
#		dp[0][index] = False
	pprint( dp)

	for row in range(1, len(s) + 1):
		for col in range(1, len(p) + 1):
			if s[row-1] == p[col-1] or p[col-1] == '?':
				dp[row][col] = dp[row-1][col-1]
				continue

			if p[col-1] == '*':
				dp[row][col] = dp[row-1][col] or dp[row][col-1]
				continue

	return dp[row][col]

#print ismatch("geeksforgeeks", "g*k**ss")
print ismatch("abceb", "*a*b")

			
				
