


def longestsub(s):
    end = 1
    cur = 0
    count = 1
    maxlen = 1
    ch = s[cur]
    maxstr = ""
    while end < len(s):
        if ch == s[end]:
            count += 1 
            if count == 2:
                if end - cur + 1 > maxlen:
                    maxlen = end-cur+1
                    maxstr = s[cur:cur+maxlen]
            elif count > 2:
                count -= 1
                cur = end - 1
        else:
            ch = s[end]
            count = 1
            if end - cur + 1 > maxlen:
                maxlen = end - cur + 1
                maxstr = s[cur:cur+maxlen]
        end += 1

    print maxlen,maxstr

    
            

s = "aabbaaaaabb"
s = "asdfghjklmnbv"
print "Testing : %s" % s
longestsub(s)
