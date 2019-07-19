

def multiply(s1, s2):
	result = []
	multiplier = 1
	for num1 in range(len(s1)-1, -1, -1):
		total = 0
		carry = 0
		totalsum = 0
		for num2 in range(len(s2)-1, -1, -1):
			total = (ord(s1[num1]) - ord('0')) * (ord(s2[num2]) - ord('0')) + carry
			if num2 > 0:
				totalsum += total % 10 * pow(10,len(s2)-1-num2) 
				if total > 10:
					carry = total / 10
			else:
				totalsum += total * pow(10,len(s2)-1)
		result.append(totalsum * multiplier)
		multiplier = multiplier * 10
	print result
	totalsum = sum(result)
	print str(totalsum)


multiply("123", "456")






