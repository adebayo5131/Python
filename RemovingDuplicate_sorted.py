class Solution(object):
    def removeDuplicates(self, nums):
        prev = 0
        for j in range(len(nums)):
            if nums[j] != nums[prev]:
                prev += 1
                nums[prev] = nums[j]
        return prev+1


n = [1, 2, 3, 4, 5, 5, 6, 6, 7]

test = Solution()
print(test.removeDuplicates(n))
