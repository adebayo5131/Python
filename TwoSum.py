class Solution(object):
    def twoSum(numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        maps = {}
        for i, num in enumerate(numbers):
            if target-num in maps:
                return (maps[target-num]+1, i+1)
            maps[num] = i
                
print(Solution.twoSum([2,3,4,5,7,9], 9))
