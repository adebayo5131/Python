#O(n) time | O(n) space
def twoSums(arr, target):
    memo = {}

    for i in arr:
        complement = target - i
        if complement in memo:
            return [complement, i]
        else:
            memo[i] = True
    return []

arr = [3, 5, -4, 8, 11, 1, -1, 6]
target = 10
print(twoSums(arr, target))
