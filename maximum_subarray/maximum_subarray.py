# https://leetcode.com/problems/maximum-subarray/

# Time: O(N^2) | Space: O(1)
def maxSubArray(nums) -> int:
    max_sum = nums[0]
    for i in range(len(nums)):
        running_sum = nums[i]
        max_sum = max(max_sum, running_sum)
        for j in range(i+1, len(nums)):
            running_sum = running_sum + nums[j]
            max_sum = max(max_sum, running_sum)

    return max_sum

# Time: O(N) | Space: O(1)
def maxSubArray2(nums) -> int:
    running_sum = 0
    max_sum = nums[0]
    for n in nums:
        if running_sum < 0:
            running_sum = 0
        running_sum += n
        max_sum = max(max_sum, running_sum)

    return max_sum

# using divide and conquer
def maxSubArray3(nums) -> int:
    pass

nums = [-1,0,-2]
maxSubArray(nums)
