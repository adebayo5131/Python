
# O(n) time complexity and O(n) space complexity


def twoNumberSum(arr, target):

    memo = {}

    for num in arr:
        complement = target - num
        if complement in memo:
            return [complement, num]
        else:
            memo[num] = True
    return []


array = [3, 5, -4, 8, 11, 1, -1, 6]
target = 10
print(twoNumberSum(array, target))
