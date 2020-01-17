# O(n) time and O(1) space
def kadanesAlgorithm(array):
    # Write your code here.
    maxEnding = array[0]
    maxSoFar = array[0]

    for i in range(1, len(array)):
        new_Sum = maxEnding + array[i]
        maxEnding = max(array[i], new_Sum)
        maxSoFar = max(maxSoFar, maxEnding)
    return maxSoFar


print(kadanesAlgorithm([3, 5, -9, 1, 3, -2, 3, 4, 7, 2, -9, 6, 3, 1, -5, 4]))
