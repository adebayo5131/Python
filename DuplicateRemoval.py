from collections import Counter


def findDuplicates(nums):
    n = len(nums)
    # off setting the values by -1 since  1 ≤ a[i] ≤ n
    for i in range(n):
        nums[i] = nums[i] - 1
    for i in range(n):
        nums[nums[i] % n] = nums[nums[i] % n] + n
    result = []
    for i in range(n):
        if nums[i] // n > 1:
            result.append(i+1)  # Index + 1 to retain the correct number
    return result

    # Or return (Counter(nums) - Counter(set(nums))).elements()


print(findDuplicates([4, 3, 2, 7, 8, 2, 3, 1]))
