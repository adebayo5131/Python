class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if not intervals:
            return []
        intervals.sort()
        newIntervals = [intervals[0]]

        for i in range(1, len(intervals)):
            if newIntervals[-1][-1] >= intervals[i][0]:
                maxEnding = max(newIntervals[-1][-1], intervals[i][1])
                newIntervals[-1][-1] = maxEnding
            else:
                newIntervals.append(intervals[i])
        return newIntervals

test = Solution()

print(test.merge([[1, 3], [2, 6], [8, 10], [15, 18]]))
