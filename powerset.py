
def addnum(res, num):
	res.append(num)
	#print res
	return res

def powerset(nums, index, res):

	if index == len(nums):
		results.append(res)
		return

	powerset(nums, index + 1, addnum(res,nums[index]))
	powerset(nums , index + 1, res)



results = [[]]

nums = [1,2,3]
res = []
powerset(nums, 0, res)
print results
