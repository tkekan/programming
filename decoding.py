


def decode(s,results,final):
    
    if not s:
        final.append(''.join(results))
        #results[:] = []
        return 
    for r in range(0,len(s)):
        temp = ord('A') + int(s[0:r+1]) - 1
        if temp > 90:
            return 
        ch = chr(temp) 
        results.append(ch)
        ret = decode(s[r+1:], results, final)
        results.pop()
        

results = []
final = []
decode('1226',results,final)
print final
