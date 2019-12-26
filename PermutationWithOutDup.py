def permuteUnique(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    permutation = []
    helper(0, nums, permutation)
    return permutation

def helper(i, arr, permutation):
    if i == len(arr) - 1:
        if arr[:] not in  permutation:
            permutation.append(arr[:])
    else:
        for j in range(i,len(arr)):
            arr[j], arr[i] = arr[i], arr[j]
            helper(i+1,arr,permutation)
            arr[j], arr[i] = arr[i], arr[j]

arr = [1, 1, 2]
print(permuteUnique(arr))
        