def minMaxSum(arr,t):
    minsum = 0
    maxSum =0

    for i in range(len(arr)-1):
        minsum+= arr[i]

    for i in range(1,len(arr)):
        maxSum += arr[i]
                      
    totalsum  = maxSum - minsum
    print(totalsum)


array = [1,2,3,9]
target = 8

minMaxSum(array, target)
