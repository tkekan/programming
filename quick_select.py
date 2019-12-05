
import random


def partition(nums,l,r,pivot):
    val = nums[pivot]
    nums[pivot],nums[r] = nums[r],nums[pivot]
    w = l
    for i in range(l,r):
        if nums[i] <= val:
            nums[w],nums[i] = nums[i],nums[w]
            w+=1
    nums[w],nums[r] = nums[r],nums[w]
    return w

def util(nums,l,r,k):
    if l > r or l == r:
        return

    pivot = random.randint(l,r)
    pivot = partition(nums,l,r,pivot)
    if pivot == k:
        return

    if k < pivot:
        return util(nums,l,pivot-1,k)
    else:
        return util(nums,pivot+1,r,k)

def kclosest(nums,k):
    util(nums,0,len(nums)-1,k)
    print nums[:k]


nums = [10,5,0,1,20,4]
k = 4
kclosest(nums,k)
