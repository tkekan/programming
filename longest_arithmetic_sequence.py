

def longest(A):
    d = [dict() for x in range(len(A))]
    maxlen = 0
    for index in range(1,len(A)):
        for j in range(0,index):
            diff = A[index] - A[j]
            if diff in d[j]:
                d[index][diff] = d[j][diff] + 1
            else:
                d[index][diff] = 2
            maxlen = max(maxlen,d[index][diff])
    return maxlen

def longest_2(A):
    n = len(A)
    llap = [2] * n
    ans = 2
    for j in range(n-2,0,-1):
        i = j - 1
        k = j + 1
        while i >= 0 and k < n:
            if A[i] + A[k] == 2 * A[j]:
                llap[j] = max(llap[k] + 1, llap[j])
                ans = max(ans,llap[j])
                i-=1
                k+=1
            elif A[i] + A[k] < 2 * A[j]:
                k+=1
            else:
                i -= 1
    print ans

A = [1,2,3,6,15,16]
print longest(A)
longest_2(A)
