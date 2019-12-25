def moveZeroes(nums):
    """
    :type nums: List[int]
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    i = 0
    j = len(nums)

    while(i < j):
        if nums[i] == 0:
            nums.pop(i)
            nums.append(0)
            j -= 1
        else:
            i += 1
    return nums

    #OR this
#         j = 0
#         for i in range(len(nums)):
#             if nums[i] != 0:
#                 nums[i], nums[j] = nums[j], nums[i]
#                 j += 1


n = [0, 1, 0, 3, 12]
print(moveZeroes(n))
