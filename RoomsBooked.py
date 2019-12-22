'''
Given A = ["+1A", "−1A", "+3F", "−3F", "+3F", "+8X"], your function should return "3F". Room 3F was booked twice, while rooms 1A and 8X were booked only once. Note that rooms 3F and 8X are still booked at the end.
Given A = ["+1A", "+3F", "+8X", "−1A", "−3F", "−8X"], your function should return "1A". All of the rooms "1A", "3F" and "8X" were booked once. "1A" is the smallest alpha-numerically out of them.
Given A = ["+0A"], your function should return "0A".
Given A = ["+9Z", "−9Z", "+9Z", "−9Z", "+9Z", "+3B"], your function should return "9Z", as room 9Z was booked three times.
'''


import sys
from collections import Counter

mapper = {
    "+": [],
    "-": []
}


def solution(A):
    dict = {}
    for rooms in A:
        if rooms[0] == "+":
            if rooms not in dict:
                dict[rooms] = 1
            else:
                dict[rooms] += 1
    i = 0
    booked = ""
    for dicRoom in dict:
        if dict[dicRoom] > i:
            i = dict[dicRoom]
            booked = dicRoom

    booked = booked.split('+')
    return booked[1]
#     """Your solution goes here."""
#     structureMap(A)
#     count = Counter(mapper["+"])
#     return count.most_common(1)[0][0]


# def structureMap(arr):
#     for i in arr:
#         if i[0] == "+":
#             mapper["+"].append("".join(i.split("+")))
#         else:
#             mapper["-"].append("".join(i.split("-")))


A = ["+1A", "+3F", "+8X", "−1A", "−3F", "−8X"]
B = ["+1A", "−1A", "+3F", "−3F", "+3F", "+8X"]
C = ["+0A"]
D = ["+9Z", "−9Z", "+9Z", "−9Z", "+9Z", "+3B"]
E = ["+9Z", "+9A", "+3E", "+4F", "+6A", "+8E",
     "-9A", "+9A", "-3E", "-4F", "-6A", "-8E"]
print(solution(E))
