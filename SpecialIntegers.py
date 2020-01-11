from collections import Counter


class Solution(object):
    def findSpecialInteger(arr):
        """
        :type arr: List[int]
        :rtype: int
        """

        count = Counter(dict)
        return count.most_common(1)[0][0]

        # max = 0
        # for i in dict:
        #     k = dict.get(i)
        #     if k > max:
        #         max = k
        #         key = i
        # return key
print(Solution.findSpecialInteger([1, 2, 2, 6, 6, 6, 6, 7, 7, 8, 8, 8, 9]))
