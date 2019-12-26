
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        
        """
        dic = {}
        for items in strs:
            sortedItems = ''.join(sorted(items))
            if sortedItems in dic:
                dic.get(sortedItems).append(items)
            else:
                dic[sortedItems] = [items]
        return dic.values()

        # for word in dic:
        #     print(dic[word])

answer = Solution()
n  = ["eat", "tea","tap" ,"tan", "ate", "nat"]
print(answer.groupAnagrams(n))
