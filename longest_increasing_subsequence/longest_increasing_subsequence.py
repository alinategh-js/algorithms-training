import math

# time: O(N^2) | space: O(N)
def lengthOfLIS(nums: list) -> int:
    lengths = [1] * len(nums)
    for i in range(len(nums)):
        temp_length = 1
        for j in range(i):
            if  nums[i] > nums[j] and lengths[j] + 1 > temp_length:
                temp_length = lengths[j] + 1
        lengths[i] = temp_length
    
    return max(lengths)

print(lengthOfLIS([0,1,0,3,2,3]))