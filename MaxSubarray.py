print('''
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
''')


def maxSubArray(self, nums):

    ult_sum =nums[0]
    for i in range(1,len(nums)): 
        nums[i]= max(nums[i], nums[i]+nums[i-1]) 
        ult_sum= max(ult_sum,nums[i]) 
    return ult_sum  
    
