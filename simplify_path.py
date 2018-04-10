
def simplify(s):
    results = []
    i = 0
    while i < len(s):
        if s[i] == '/':
            i+=1
            continue
        if s[i] == '.':
            if s[i + 1] == '.':
                results.pop()
            i+=1
            continue
        else:
            nexti = s.find('/',i)
            if nexti > 0:
                results.append(s[i:nexti])
            else:
                results.append(s[i:])
                break
            i = nexti
            continue
    print results 




s = "/dir1/dir2/./dir3/../dir4/.././dir5"
simplify(s)
