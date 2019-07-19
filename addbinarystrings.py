
def addstrings(str1, str2):
	str1 = list(str1)
	str2 = list(str2)
	carry = 0
	out = ''
	while len(str1) or len(str2):
		if len(str1):
			num1 = ord(str1.pop()) - ord('0')
		else:
			num1 = 0
		if len(str2):
			num2 = ord(str2.pop()) - ord('0')
		else:
			num2 = 0
		totalsum = num1 + num2 + carry
		out = chr(ord('0') + (totalsum % 2)) + out
		carry = totalsum / 2
	if carry > 0:
		out = '1' + out
	print "\n", out









str1 = "111000"
str2 = "10"
addstrings(str1, str2)
