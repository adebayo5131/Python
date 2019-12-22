def Sort(arr):
    last = len(arr)
    start = 0
    quickSort(arr, start, last - 1)
    return arr


def quickSort(arr, start, last):
    if start < last:
        part = partition(arr, start, last)
        quickSort(arr, start, part-1)
        quickSort(arr, part + 1, last)
    return arr


def partition(arr, start, last):
    i = start - 1
    pivot = arr[last]

    for j in range(start, last):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[last] = arr[last], arr[i + 1]
    return (i + 1)


n = [2, 5, 7, 9, 0, 3, 1, 4, 5, 7, 8, 3, 4, 5, 2, 4, 5, 6]
print(Sort(n))
