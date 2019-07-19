


#inputs = [1, 9, 3, 10, 4, 20, 2]
inputs = [36, 41, 56, 35, 44, 33, 34, 92, 43, 32, 42, 1, 9, 3, 10, 4, 20, 2]

def longest_sequence(inputs):
    dic = dict()
    for items in inputs:
        dic[items] = True
    
    maxlen = 0
    for items in dic.keys():
        if items - 1 not in dic:
            leng = 1
            while items + 1 in dic:
                leng += 1
                items += 1
            maxlen = max(maxlen, leng)
    print "Maxlength: %d" % maxlen


longest_sequence(inputs)
              
