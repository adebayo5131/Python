class Solution:

    #Faster solution Binary Search B_S found online 24ms
    def B_S(self, nums, target, start, end):
        mid = start + ((end - start) // 2)

        if target == nums[mid] or target > nums[mid - 1] and target <= nums[mid]:
            return mid
        elif target > nums[mid] and target <= nums[mid + 1]:
            return mid + 1
        elif nums[mid] > target:
            return self.B_S(nums, target, start, mid - 1)
        else:
            return self.B_S(nums, target, mid + 1, end)

    def searchInsert(self, nums, target):
        if target <= nums[0]:
            return 0
        elif target > nums[-1]:
            return len(nums)

        findIndex = self.B_S(nums, target, 0, len(nums) - 1)
        return findIndex

    #My solution slow 40 ms
    def S_I(self, nums, target):
        count = 0
        for i in range(len(nums)):
            if nums[i] == target:
                return i
            else:
                if target > nums[i]:
                    count+=1
        return count


def main():
    solution = Solution()
    print(solution.searchInsert([1, 3, 5, 6], 7))

    mySolution = Solution()
    print(mySolution.S_I([1, 3, 5, 6], 7))


if __name__ == '__main__':
    main()

