



def modify(num , s):
    if num > 0:
        if num % 2 == 0:
            s = s + "0"
        else:
            s = s + "1"
        print "value is %s"  %s
        modify(num - 1, s)
        print "value is %s"  %s

s = ""
modify(5, s)
print s

 
