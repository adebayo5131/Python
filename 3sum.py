# Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0?
# Find all unique triplets in the array which gives the sum of zero.

# Note:

# The solution set must not contain duplicate triplets.


def threeSum(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    # nums.sort()
    space = []
    for i in range(len(nums)-1):
        if i == 0 or i > 0 and nums[i - 1] != nums[i]:
            left = i+1
            right = len(nums) - 1
            while left < right:
                Sum = nums[i] + nums[left] + nums[right]
                if Sum == 0:
                    space.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while right > left and nums[right] == nums[right + 1]:
                        right -= 1
                elif Sum < 0:
                    left += 1
                else:
                    right -= 1
    return space


print(threeSum([0, -1, -1, 2, -3, 1]))
