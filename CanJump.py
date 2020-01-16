
def canJump(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    jump = 1
    for i in reversed(range(len(nums)-1)):
        if nums[i] < jump:
            jump += 1
        else:
            jump = 1
    return jump == 1

print(canJump([2,3,1,1,4]))