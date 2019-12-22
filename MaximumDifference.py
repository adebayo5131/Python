def MaxDiff(arr):

    if arr == []:
        return 0
    if len(arr) == 1:
        return 0
    if max(arr) == arr[0]:
        arr.remove(arr[0])

    minNum = arr[0]
    maxNum = arr[0]
    for i in range(len(arr)):
        minNum = min(minNum, arr[i])
        maxNum = max(maxNum, arr[i])
    return (maxNum - minNum)


n = [100, 40, 90, 10]
print(MaxDiff(n))
