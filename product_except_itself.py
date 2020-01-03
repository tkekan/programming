
def productExceptSelf(nums):
	#first lets create the output array using mult from right
	out = [0]*len(nums)
	start = 1

	#accumulate the mult from right in out array
	for i in xrange(len(nums)-1,-1,-1):
		out[i] = start
		start *= nums[i]

	#now maintain leftMult variable and use it for every index in out array
	leftMult = 1
	for i in xrange(len(out)):
		out[i] *= leftMult
		leftMult*=nums[i]
	return out


nums = [1,2,3,4]
productExceptSelf(nums)
