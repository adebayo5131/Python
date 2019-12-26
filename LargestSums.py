def threeLargestSum(arr):
    threeSums = [None, None, None]
    for num in arr:
        update(threeSums, num)
    return threeSums


def update(threeSums, num):
    if threeSums[2] is None or num > threeSums[2]:
        shiftUpdate(threeSums, num, 2)
    elif threeSums[1] is None or num > threeSums[1]:
        shiftUpdate(threeSums, num, 1)
    elif threeSums[0] is None or num > threeSums[0]:
        shiftUpdate(threeSums, num, 0)


def shiftUpdate(array, num, positions):

    for i in range(positions + 1):
        if i == positions:
            array[i] = num
        else:
            array[i] = array[i + 1]


arr = [141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7]
print(threeLargestSum(arr))
