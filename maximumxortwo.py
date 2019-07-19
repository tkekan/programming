import pdb

def findMaximumXOR(nums):
    answer = 0
    for i in range(5)[::-1]:
        answer <<= 1
	pdb.set_trace()
        prefixes = {num >> i for num in nums}
        answer += any(answer^1 ^ p in prefixes for p in prefixes)
    return answer

nums = [3,10,5,13,2,15]
res = findMaximumXOR(nums)
print res
