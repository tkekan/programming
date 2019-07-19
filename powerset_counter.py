




def powerset(nums):
	size = pow(2,len(nums))
	results = []
	for index in range(0, size):
		res = []
		for counter in range(0,len(nums)):
			if index & (1 << counter):
				res.append(nums[counter])
		results.append(res)
	print results, len(results)

nums = [1,2,3]
powerset(nums)
