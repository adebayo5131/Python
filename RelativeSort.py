
def relativeSortArray(arr1, arr2):

    memo = dict()
    returnValue = list()

    for i in arr1:
        if i in memo:
            memo[i] += 1
        else:
            memo[i] = 1

    for i in arr2:
        if i in memo:
            returnValue.extend([i] * memo.pop(i))

    for i in memo.keys():
        returnValue.extend([i]*memo[i])
    return returnValue


arr1 = [2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19]
arr2 = [2, 1, 4, 3, 9, 6]
print(relativeSortArray(arr1, arr2))
# [2,2,2,1,4,3,3,9,6,7,19]
