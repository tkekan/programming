


def inputs(itr):
    d = {}
    for i in range(0, len(itr)):
        if itr[i] not in d.keys():
            d[itr[i]] = 1
        else:
            d[itr[i]] += 1
    for key,values in sorted(d.items(),key = lambda x: x[1]):
        print key,values

itr = "1. Hi how are you. What are you doing today ?"
inputs(itr)
