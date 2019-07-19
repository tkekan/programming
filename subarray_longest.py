

def longest(arr, k):
	dic = {}
	maxlen = 0
	sum = 0
	for index in range(len(arr)):
		sum += arr[index]
  		
		if sum == k:
 		    maxlen = max(maxlen, index + 1)
		if sum not in dic:
			dic[sum] = index

		dsum = sum - k
		if dsum in dic:
			maxlen = max(maxlen, index - dic[dsum])
	
	print maxlen
			
		
	


arr = [1, -1, 5, -2, 3]
k = 3
longest(arr, 3)
