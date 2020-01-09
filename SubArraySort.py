
# Time Complexity O(n) and space Complexity O(1)


def subarraySort(array):
    minOutOfOrder = float("inf")
    maxOutOfOrder = float("-inf")

    for i in range(len(array)):
        num = array[i]
        if outOfOrder(i, num, array):
            minOutOfOrder = min(minOutOfOrder, num)
            maxOutOfOrder = max(maxOutOfOrder, num)

    if minOutOfOrder == float("-inf"):
        return [-1, -1]

    leftOutOfOrder = 0
    while minOutOfOrder >= array[leftOutOfOrder]:
        leftOutOfOrder += 1

    rightOutOfOrder = len(array)-1
    while maxOutOfOrder <= array[rightOutOfOrder]:
        rightOutOfOrder -= 1

    return [leftOutOfOrder, rightOutOfOrder]


def outOfOrder(index, num, array):
    if index == 0:
        return num > array[index+1]
    if index == len(array)-1:
        return num < array[index-1]
    return num > array[index+1] or num < array[index-1]


print(subarraySort([1, 2, 4, 7, 10, 11, 7, 12, 7, 7, 16, 18, 19]))
