def findDuplicate(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    slow = nums[0]
    fast = nums[nums[0]]
    while slow != fast:
        slow = nums[slow]
        fast = nums[nums[fast]]

    fast = 0
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]
    return slow


print(findDuplicate([2, 5, 9, 6, 9, 3, 8, 9, 7, 1]))
