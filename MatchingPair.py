#O(n^2) | O(n) space
def findmatching(arr, t):
    sums = []
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i]+ arr[j] == t:
               sums.append(sorted([arr[i], arr[j]]))
    return sums
            


t = 16
arr = [11, 15,1, 6, 8, 9, 10]
print(findmatching(arr,t))
