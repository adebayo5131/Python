class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        indexes = [-1, -1]
        if not nums:
            return indexes

        if len(nums) == 1:
            if nums[0] == target:
                indexes[0] = 0
                indexes[1] = 0
                return indexes
            else:
                return indexes

        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right)//2
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                # expand to left
                while nums[left] != target:
                    left += 1
                indexes[0] = left
                # expand to right
                while nums[right] != target:
                    right -= 1
                indexes[1] = right
                return indexes

        return [-1, -1]


test = Solution()
nums = [5, 7, 7, 8, 8, 10]
target = 8
print(test.searchRange(nums, target))
