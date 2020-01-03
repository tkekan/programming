from collections import defaultdict


def printwords(words, string, out, d):
    if len(string) == 0:
        print out + "\n"
        return []

    if string in d:
        for w in d[string]:
            out = out + " " + w
        print out + "\n"
        return d[string]

    for index in range(1, len(string) + 1):
        temp = list(string)
        prefix = ''.join(temp[0:index])
       
        if prefix in words:
            ret = printwords(words, ''.join(temp[index:]), out + prefix + " ", d)
            d[string].append(prefix)
            for w in ret:
                d[string].append(w)
    return d[string]

words = { "this":0, "th":0, "is":0,"famous":0, "Word":0, "break" :0 , "b":0, "Wordis":0, "is":0,
		  "r":0, "e":0, "a":0, "k":0, "br":0, "bre":0, "brea":0, "ak":0, "problem":0, "breaking":0, "king":0 }

#string = "Wordbreakproblem"
string = "thisWordisbreaking"
string = "catssanddog"
words = {'cat':0,'cats':0,'sand':0,'and':0,'dog':0}
d = defaultdict(list)
printwords(words, string, "", d)
