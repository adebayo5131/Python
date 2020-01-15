# #Slower Solution O(N^2)
# class MyCalendar(object):

#     def __init__(self):
#         self.successful_bookings = []

#     def book(self, start, end):
#         for prevStart, prevEnd in self.successful_bookings:
#             if prevStart < end and start < prevEnd:
#                 return False
#         self.successful_bookings.append((start,end))
#         return True

# Using Binary Search


class MyCalendar(object):

    def __init__(self):
        self.successful_Bookings = []
        self.success = []

    def getIndex(self, start, end):
        left = 0
        right = len(self.successful_Bookings) - 1
        while left <= right:
            mid_point = (left + right) // 2
            mid_start, mid_end = self.successful_Bookings[mid_point]
            if start >= mid_end:
                left = mid_point + 1
            elif end <= mid_start:
                right = mid_point - 1
            else:
                return -1
        return left

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        i = self.getIndex(start, end)
        if i == -1:
            self.success.append(False)
            return False
        self.successful_Bookings.insert(i, (start, end))
        self.success.append(True)
        return True


test = MyCalendar()
test.book(47, 50)
test.book(33, 41)
test.book(39, 45)
test.book(33, 42)
test.book(25, 32)
test.book(26, 35)
test.book(19, 25)
test.book(3, 8)
test.book(8, 13)
test.book(18, 27)
print(test.successful_Bookings)
print(test.success)
