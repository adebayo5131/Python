class Solution(object):
    def find132pattern(nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        pairs = []
        checker = float("-inf")
        for element in reversed(nums):
            if element < checker:
                return True
            while pairs and pairs[-1] < element:
                checker = pairs.pop()
            pairs.append(element)
        return False


print(Solution.find132pattern([3, 1, 4, 2]))
