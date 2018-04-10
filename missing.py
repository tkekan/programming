#Array of size n contains number 1..n
# Find the missing number



def find(nums):
    l = len(nums)
    for i in range(0, l):
        m = abs(nums[i]) - 1
        if nums[m] > 0:
            nums[m] = -nums[m]
        else:
            nums[m] = nums[m]

    results = []
    for i in range(0, l):
       if nums[i] > 0:
           results.append(i+1)
    print results


nums = [4,3,2,7,8,2,3,1]
find(nums)
