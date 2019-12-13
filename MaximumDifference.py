def MaxDiff(arr):
    # if max(arr) == arr[0]:
    #     arr.remove(arr[0])
    # if arr == []:
    #     return 0
    # if len(arr) == 1:
    #     return 0

    # j = 0
    # for i in range(1, len(arr)):
    #     maxNum = arr[j]
    #     if arr[i] > maxNum:
    #         maxNum = arr[i]
    #         j += 1

    # arr = arr[:i]

    # minNum = min(arr)

    # return maxNum - minNum
    if max(arr) == arr[0]:
        arr.remove(arr[0])

    minNum = arr[0]
    maxNum = arr[0]
    for i in range(1, len(arr)):
        minNum = min(minNum, arr[i])
        maxNum = max(maxNum, arr[i])
    return (maxNum - minNum)


n = [100,40,90]
print(MaxDiff(n))
