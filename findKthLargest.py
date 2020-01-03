import random


def part(nums, l , r, p):
    pi = nums[p]
    nums[r], nums[p] = nums[p], nums[r]
    
    w = l
    for i in range(l, r):
        if nums[i] <= pi:
            nums[w], nums[i] = nums[i], nums[w]
            w+=1
    nums[w], nums[r] = nums[r] , nums[w]
    return w
def util( nums, l, r, k):
    if l == r:
        return nums[l]
    #p = random.randint(l, r)
    p = nums[r]
    start = l
    end = r
    while True:
        while nums[start] < p and start < end:
            start+=1
        while nums[end] >= p and start < end:
            end-=1
        if start == end:
            break
        nums[start],nums[end] = nums[end],nums[start]

    nums[start],nums[r] = nums[r],nums[start]

    if start + 1 == k:
        return p
    if k < start + 1:
        return util(nums, l, start-1, k)
    else:
        return util(nums, start+1, r, k)

nums = [3,2,5,1,2,1,1,1,2,3,2,4,5,5,6,6,5,7]
k = 4
print util(nums, 0, len(nums)-1, len(nums)-k)

"""

def p_sort(nums, l , r, p):
    w = l
    pi = nums[p]
    nums[p],nums[r] = nums[r],nums[p]
    for i in range(l,r+1):
        if nums[i] <= pi:
            nums[w],nums[i] = nums[i],nums[w]
            w+=1

    nums[w],nums[r] = nums[r],nums[w]
    return w
    




def partition(nums, k):
    l = 0
    r = len(nums) - 1 
    if l == r:
        return nums[l]
    p = random.randint(l,r)
    p = p_sort(nums, l, r, p)
    if p == k:
        print nums[p]
        return
    if p < k:
        return partition(nums[p+1:],k)
    else:
        return partition(nums[:p], k)



nums = [3,2,3,1,2,4,3,5,6,7]
partition(nums,4) """
