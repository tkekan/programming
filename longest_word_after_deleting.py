
def isSubSeq(word, string):
    j = 0
    for index in range(0,len(string)):
        if string[index] == word[j]:
            j+=1
            if j == len(word):
                break
    return j == len(word)

def findlongest(string, dic):
    length = 0
    word = None
    for words in dic.keys():
        if isSubSeq(words, string) and len(words) >= length:
            if len(words) > length:
                word = words
            else:
                word = (words,word)[word < words]
            length = len(words)
    print word    



dic = {"ale":0, "apple":0, "monkey":0, "plea":0};
string = "abpcplea"
findlongest(string, dic)
