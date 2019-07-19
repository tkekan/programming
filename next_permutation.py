
def findnext(string):
	pos = -1
	for index in range(len(string)-1, 0, -1):
		if int(string[index-1]) < int(string[index]):
			pos = index -1
			break

	if pos == -1:
		print "Not possible"
		return

	swappos = -1
	for index in range(len(string)-1, pos, -1):
		if int(string[index]) > int(string[pos]):
			swappos = index
			break

	print swappos

	number = list(string)
	number[pos],number[swappos] = number[swappos],number[pos]
	left = pos + 1
	end = len(string) -1
	while left <= end:
		number[left],number[end] = number[end],number[left]
		left += 1
		end -= 1

	print ''.join(number)








string = "132"
findnext(string)
