

def compare(countp, countw, index, M):
    if countp == countw:
        print "Found at index: %d" % (index-M)

def findpattern(pattern , text):
    countp = [0] * 255
    countw = [0] * 255
    for index in range(0,len(pattern)):
        countp[ord(pattern[index])] += 1
        countw[ord(text[index])] += 1

    for index in range(len(pattern), len(text)):
        compare(countp, countw, index, len(pattern))
        countw[ord(text[index])] += 1
        countw[ord(text[index - len(pattern)])] -= 1

    compare(countp, countw, index + 1, len(pattern))






pattern = "ABCD"
pattern = "AABA"
text = "AAABABAA"
#text = "BACDGABCDA"
print "pattern %s : text : %s" %(pattern, text)
findpattern(pattern, text)
