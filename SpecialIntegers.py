from collections import Counter


class Solution(object):
    def findSpecialInteger(arr):
        """
        :type arr: List[int]
        :rtype: int
        """

        if arr is None:
            return []
        elif len(arr) == 1:
            return arr[0]
        elif len(arr) == 2:
            if arr[0] == arr[1]:
                return arr[0]
            else:
                return []
        dict = {}

        for i in arr:
            if i in dict:
                dict[i] += 1
            else:
                dict[i] = 1
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
