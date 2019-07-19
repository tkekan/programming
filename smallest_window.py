
import sys

def smallest_window(inputs, pattern):
	inputs = inputs.lower()
	pattern = pattern.lower()
	hash_input = [0 for x in range(256)]
	hash_pattern = [0 for x in range(256)]
	length = len(pattern)
	count = 0
	start = 0
	for index in range(len(pattern)):
		#i = ord(pattern[index]) - ord('a')
		i = ord(pattern[index])
		hash_pattern[i] += 1
	print hash_pattern
	
	windowlen = sys.maxint
	retstr = ''
	for j in range(0, len(inputs)):
		#if hash_input[j] == ' ':
		#	continue
		#index = ord(inputs[j]) - ord('a')
		index = ord(inputs[j])
		hash_input[index] += 1

		#print hash_pattern, hash_input, '\n'
		if ( hash_input[index] <= hash_pattern[index]
			and hash_pattern[index] != 0) :
			count += 1

		if length == count:
			#print "length == count"
			#skip_index = ord(inputs[start]) - ord('a')
			skip_index = ord(inputs[start])
			while (hash_input[skip_index] > hash_pattern[skip_index]  or
				hash_pattern[skip_index] == 0):
				if hash_input[skip_index] > hash_pattern[skip_index]:
					hash_input[skip_index] -= 1
				start += 1
				#skip_index = ord(inputs[start]) - ord('a')
				skip_index = ord(inputs[start]) 
			
			if j - start + 1 < windowlen:
				windowlen = min(windowlen, j - start + 1)
				retstr = inputs[start:j+1]
	print retstr
	return [ sys.maxint if windowlen == sys.maxint else windowlen ]


s = "This is a test string"
p = "tist"
print smallest_window(s,p)    			
