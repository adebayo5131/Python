# O(logn) time and O(1) space
def binarySearch(arr, target):
    return helper(arr, target, 0, len(arr)-1)


def helper(array, target, left, right):
    while left <= right:
        middle = (left+right)//2
        match = array[middle]
        if target == match:
            return middle
        elif target < match:
            right = middle - 1
        else:
            left = middle + 1
    return -1


print(binarySearch([0, 1, 21, 33, 45, 45, 61, 71, 72, 73], 33))
