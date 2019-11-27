class Solution:
    def longestCommonPrefix(self, strs):

        if not strs: 
            return ""
        if len(strs) == 1:
            return strs[0]
        strs.sort()
        p = ""
        for i, j in zip(strs[0], strs[-1]):
            if i == j:
                p+=i
            else:
                break
        return p

check = Solution()
str = ["Flowers", "Floor", "Flora"]
print(check.longestCommonPrefix(str))
