'''
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
'''


class Solution(object):
    def maxSubArray(nums):

        largestSum = nums[0]

        for i in range(1, len(nums)):
            nums[i] = max(nums[i], nums[i]+nums[i-1])
            largestSum = max(largestSum, nums[i])
        return largestSum


array = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(Solution.maxSubArray(array))
