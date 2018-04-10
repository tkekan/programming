

def valid(s):
	counter = { '(':0,')':0,'[':0,']':0,'{':0,'}':0 }
	maps = { '(':')', '[':']','{':'}'}

	for i in range(0, len(s)):
		counter[s[i]]+=1
	count = 0
	for keys in maps.keys():
		count = count + counter[keys] - counter[maps[keys]]

	return count == 0


val = valid('()()()([])')
print val
