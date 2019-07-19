




def printwords(words, string, out):
	if len(string) == 0:
		print out + "\n"
		return out

	for index in range(1, len(string) + 1):
		temp = list(string)
		prefix = ''.join(temp[0:index])
		if prefix in words:
			printwords(words, ''.join(temp[index:]), out + prefix + " ")

	return
words = { "this":0, "th":0, "is":0,"famous":0, "Word":0, "break" :0 , "b":0, "Wordis":0, "is":0,
		  "r":0, "e":0, "a":0, "k":0, "br":0, "bre":0, "brea":0, "ak":0, "problem":0, "breaking":0 }

#string = "Wordbreakproblem"
string = "thisWordisbreaking"
printwords(words, string, "")
