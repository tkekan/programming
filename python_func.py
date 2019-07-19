
map = {'1': new,
       '2': isf}

def new():
    print "Is called"

def isf():
    print "isf called"


for keys in map:
    map[keys]()


