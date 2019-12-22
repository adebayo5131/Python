def find_duplicates(arr1, arr2):

    # Time complexity is O(nlogn)
    # Space complexity is O(n)

    if arr1 is None or arr2 is None:
        return []

    if arr1 == arr2:
        return arr1

    nums = arr1 + arr2
    memo = {}
    array = []

    for i in range(len(nums)):  # O(n)
        if nums[i] in memo:
            memo[nums[i]] += 1
        else:
            memo[nums[i]] = 1

    for i in memo:  # O(n)
        if memo[i] > 1:
            array.append(i)

    return sorted(array)


arr1 = [1, 2, 3, 5, 6, 7]
arr2 = [3, 6, 7, 8, 20]
print(find_duplicates(arr1, arr2))


# function getDifferentNumber(arr):
#     n = arr.length

#     # since weâ€™re not allowed to modify arr, we create a copy of it
#     arrSorted = new Array(arr)

#     # sort the duplicate array in an ascending order
#     arrSorted.sort()

#     for i from 0 to n - 1:
#         if (arrSorted[i] != i):
#             return i  # i isnâ€™t in arr, hence we can return it

#     # we got here since every number from 0 to n-1 is in arr.
#     # By definition then, n isnâ€™t in arr. Otherwise, the size of arr
#     # would have been n+1 and not n.
#     return n
