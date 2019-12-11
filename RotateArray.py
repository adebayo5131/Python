def rotate(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    # nums.reverse()
    # y =nums[k:len(nums)]
    # y.reverse()
    # n = sorted(nums[0:k])
    # print(n+y)
    k = k % len(nums)
    nums[k: ], nums[:k] = nums[:-k], nums[-k:]
    print(nums)

n = [1,2,3,4,5,6,7,8,9]
k=3
rotate(n,3)
