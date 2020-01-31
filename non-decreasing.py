class Solution:
    def checkPossibility(nums):
        found = 0
        for i in range(1, len(nums)):
            if nums[i-1] > nums[i]:
                found += 1
                if i < 2 or nums[i-2] <= nums[i]:
                    nums[i-1] = nums[i]
                else:
                    nums[i] = nums[i-1]
                if found > 1:
                    return False
        return True


print(Solution.checkPossibility([4, 2, 3]))
