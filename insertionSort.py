def ascendingOrder(arr):
    for i in range(1, len(arr)):
        temp = arr[i]
        j = i - 1
        while j>=0 and arr[j] > temp:
             arr[j+1] = arr[j]
             j-= 1
             arr[j+1]= temp
             
    return arr

numbers = [5,2,4,6,1,3]
print(ascendingOrder(numbers))


