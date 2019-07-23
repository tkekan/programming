
def max_volume(nums):
    totalwater = 0
    lmax = -1
    rmax = -1
    left = 0
    right = len(nums) - 1
    while left < right:
        if nums[left] < nums[right]:
            if lmax < nums[left]:
                lmax = max(lmax,nums[left])
            else:
                totalwater += lmax - nums[left]
            left += 1
        else:
            if rmax < nums[right]:
                rmax = max(rmax, nums[right])
            else:
                totalwater += rmax - nums[right]
            right -= 1
    print totalwater






nums = [2,0,2]
nums = [3, 0, 0, 2, 0, 4]
max_volume(nums)
