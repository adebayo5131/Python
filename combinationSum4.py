
def combinationSum4(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    nums.sort()
    dp = [0] * (target + 1)

    dp[0] = 1

    for i in range(1, len(dp)):
        for num in nums:
            if num <= i:
                dp[i] += dp[i - num]
    return dp[target]


print(combinationSum4([1, 2, 3], 4))
