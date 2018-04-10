


def longest(a):
    map = {}
    for items in a:
        map[items] = items + 1

    maxLen = 1
    for keys in map.keys():
        current = 0
        try:
            while map[keys]:
                current += 1
                keys = map[keys]
        except Exception as e:
            maxLen = max(maxLen, current)
            pass

    print "Max Length : %d" %maxLen





#a = [1, 9, 3, 10, 4, 20, 2]
a = [36, 1, 56, 35, 44, 33, 39, 92, 43, 32, 52]
longest(a)
