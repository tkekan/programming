
def single(nums):
    ones = 0
    twos = 0
    for i in range(0, len(nums)):
        twos = twos | ( ones & nums[i] )
        ones = ones ^ nums[i]
        third = ~( ones & twos )
        ones = ones & third
        twos = twos & third
    return ones


nums = [2,4,2,2,3,4,5,4,5,6,5,3,3]
print(single(nums))
