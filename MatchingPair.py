#O(n^2) | O(n) space
def findmatching(arr, t):
    # sums = []
    # for i in range(len(arr)):
    #     for j in range(i+1, len(arr)):
    #         if arr[i]+ arr[j] == t:
    #            sums.append(sorted([arr[i], arr[j]]))
    # return sums
    arr.sort()

    left = 0
    right = len(arr) - 1
    pairs = []
    while left < right:
        sums = arr[left] + arr[right]
        if sums == t:
            pairs.append([arr[left], arr[right]])
        if sums > t:
            right -= 1
        else:
            left += 1
    return pairs
        

t = 16
arr = [11, 15,1, 6, 8, 9, 10]
print(findmatching(arr,t))