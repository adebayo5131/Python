class Solution:
    def twoSum(self, nums, target):
  
        dictionary  = {}
        for i, num in enumerate(nums):
            sum = target - num
            if sum in dictionary:
                return [dictionary[sum], i]
            else:
                dictionary[num] = i

a = [11,7,8,2]
t = 9
s = Solution()
print(s.twoSum(a,t))

