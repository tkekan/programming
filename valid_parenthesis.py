

def valid(s):
	counter = { '(':0,')':0,'[':0,']':0,'{':0,'}':0 }
	maps = { '(':')', '[':']','{':'}'}

	for i in range(0, len(s)):
		counter[s[i]]+=1
	count = 0
	for keys in maps.keys():
		count = count + counter[keys] - counter[maps[keys]]

	return count == 0

def valid2(s):
    cnt = 0
    for index in range(len(s)):
        if s[index] == '(' or s[index] == '[':
            cnt += 1
        elif s[index] == ')' or s[index] == ']':
            cnt -= 1
        if cnt < 0:
            return False
    return cnt == 0

val = valid2('()()()([])')
print val
