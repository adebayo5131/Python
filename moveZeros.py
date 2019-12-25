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


n = [0, 1, 0, 3, 12]
print(moveZeroes(n))
