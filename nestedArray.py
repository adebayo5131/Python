def arrayNesting(nums):
    if not nums:
        return 0

    seen = set()

    longest = float('-inf')
    for i in range(len(nums)):
        if nums[i] not in seen:
            countlongest = 0
            while nums[i] not in seen:
                seen.add(nums[i])
                i = nums[i]
                countlongest += 1
            longest = max(longest, countlongest)
    return longest


A = [5, 4, 0, 3, 1, 6, 2]
print(arrayNesting(A))
