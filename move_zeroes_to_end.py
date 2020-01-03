


def move(nums):
    w = 0
    for index in range(0,len(nums)):
        if nums[index] == 1:
            nums[w],nums[index] = nums[index],nums[w]
            w += 1
    print nums





n = [0,1,0,1,0,0,1]
n = [1,1,1,1,0]
n = [0,0,0,0,0,1]
move(n)
