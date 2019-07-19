


def longest(inputs, k):
    total = 0
    maxlen = 0
    dic = dict()
    for index in range(0, len(inputs)):
        total += inputs[index]

        if total == k:
            maxlen = index + 1
            print "Found maxlen to: " ,(maxlen, inputs[0:index + 1])
        
        dic[total] = index

        if (total - k) in dic:
            maxlen = max(maxlen, index - dic[total - k])
            arr = inputs[dic[total-k] + 1: index + 1]
            print "Updated maxlen to : ", (maxlen,arr)


inputs = [10, 5, 2, 7, 1, 9]
k = 15
longest(inputs, k)
