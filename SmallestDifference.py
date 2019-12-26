
# Time Complexity O(nlog(n) + mlog(m)) because we are sorting both arrays || space complexity O(1) sorting in place and keeping track


def smallestDifference(arrayOne, arrayTwo):

    arrayOne.sort()
    arrayTwo.sort()
    i = 0
    j = 0
    smallestDiff = float("inf")
    currentDiff = float("inf")
    smallestPairs = []

    while i < len(arrayOne) and j < len(arrayTwo):
        firstNum = arrayOne[i]
        secondNum = arrayTwo[j]
        if firstNum < secondNum:
            currentDiff = secondNum - firstNum
            i += 1
        elif firstNum > secondNum:
            currentDiff = firstNum - secondNum
            j += 1
        else:
            return [firstNum, secondNum]

        if smallestDiff > currentDiff:
            smallestDiff = currentDiff
            smallestPairs = [firstNum, secondNum]
    return smallestPairs

    # if len(a) == 0 or len(b) == 0:
    #     return 0
    # if a == [] or b == []:
    #     return []

    # current_diff = float("inf")
    # diff = 0
    # array = [0]*2
    # for i in a:
    #     for j in b:
    #         diff = abs(j-i)
    #         if diff < current_diff:
    #             current_diff = min(current_diff, diff)
    #             array[0] = i
    #             array[1] = j

    # return array


a = [-1, 5, 10, 20, 28, 3]
b = [26, 134, 135, 15, 17]
print(smallestDifference(a, b))
