def threeSumClosest(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    
    nums.sort()
    checker = float("inf")
    for i in range(len(nums)):
        left = i+1
        right = len(nums)-1
        while left < right:
            sums = nums[i] + nums[left] + nums[right]
            if sums == target:
                return sums
            elif sums < target:
                left+=1
            else:
                right-=1
                
            if abs(sums-target) < abs(checker-target):
                checker = sums
    return checker
print(threeSumClosest([-1, 2, 1, -4],1))
