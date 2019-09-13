
def addnum(res, num):
	res.append(num)
	#print res
	return res

def powerset(nums, index, res):
    if index == len(nums):
        results.append(list(res))
        return

    results.append(list(res))
    for i in range(index,len(nums)):
        res.append(nums[i])
        powerset(nums, i + 1,res) 
        res.pop()



results = []

nums = [1,2,3]
res = []
powerset(nums, 0, res)
print results
