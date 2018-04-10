


class Name:
    class __name:
        def __init__(self, arg):
            print "__name start"
            self.val = arg
            print "__name done"
        def __str__(self):
            print "__str__ __name called"
            return repr(self) + str(self.val)
    instance = None
    def __init__(self, arg):
        if Name.instance == None:
            print "init none"
            Name.instance = Name.__name(arg)
            print "init none done"
        else:
            print "init non none"
            Name.instance.val = arg
            print "init non none done"
#    def __getattr__(self, name):
#        print "getattr"
#        return getattr(self.instance, name)

print "creating n1"
n1 = Name(100)
print "creating n1 done"
print "printing n1"
print (n1)
print "printing n1 done"
n2 = Name(200)
print (n2)
