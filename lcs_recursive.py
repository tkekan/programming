


def find(str1,str2,m,n):
    if m < 0 or n < 0 :
        return 0
    elif str1[m] == str2[n]:
        return 1 + find(str1,str2,m-1,n-1)    
    else:
        return max(find(str1,str2,m-1,n), find(str1,str2,m,n-1))


str1 = "AGGTAB"
str2 = "GXTXAYB"
print find(str1,str2,len(str1) - 1,len(str2) - 1)

