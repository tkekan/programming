

def sort012(nums):
    l = 0
    mid = 0
    h = len(nums) -1
    while mid <= h:
        if nums[mid] == 0:
            nums[l],nums[mid] = nums[mid],nums[l]
            l += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1
        else:
            nums[mid],nums[h] = nums[h],nums[mid]
            h -= 1
    print nums


nums = [0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]
sort012(nums)
