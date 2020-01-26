class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums:
            return [-1, -1]

        if len(nums) == 1:
            if nums[0] == target:
                return [0, 0]
            else:
                return [-1, -1]

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
                # expand to right
                while nums[right] != target:
                    right -= 1
                return [left, right]

        return [-1, -1]


test = Solution()
nums = [5, 7, 7, 8, 8, 10]
target = 8
print(test.searchRange(nums, target))
