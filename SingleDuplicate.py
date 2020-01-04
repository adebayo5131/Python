def singleNonDuplicate(nums):
    left = 0 
    right = len(nums) - 1
    while left < right:
        middle = (left + right) // 2
        if middle % 2 == 0:
            if nums[middle] != nums[middle + 1]:
                right = middle
            else:
                left = middle + 1
        else:
            if nums[middle] != nums[middle - 1]:
                right = middle
            else:
                left = middle + 1

    return nums[left]

print(singleNonDuplicate( [1,1,2,3,3,4,4,8,8]))