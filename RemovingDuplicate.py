class Solution(object):
    def removeDuplicates(self, nums,val):
        i = 0
        for j in range(len(nums)):
            if nums[i] is val :
                del nums[i]
            else:
                i+=1
        return nums
        

n = [3,2,2,3]
v = 3
y = Solution()
print(y.removeDuplicates(n,v))
