class Solution(object):
    def topKFrequent(self, nums, k):
        if len(nums) == 1 and k == 1:
            return [nums[0]]
        elif not nums:
            return

        memo = dict()

        for i in nums:
            if i in memo:
                memo[i] += 1
            else:
                memo[i] = 1

        frequency = dict()
        for key, values in memo.items():
            if values in frequency:
                frequency[values].append(key)
            else:
                frequency[values] = [key]

        kthLargest = []
        for i in range(len(nums), -1, -1):
            if i in frequency:
                kthLargest += frequency[i]
            if len(kthLargest) >= k:
                break
        return kthLargest[:k]


test = Solution()
print(test.topKFrequent([1, 1, 1, 2, 2, 3], 2))
