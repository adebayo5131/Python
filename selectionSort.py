import time
start_time = time.time()


def selectionSort(arr):
    for i in range(len(arr)):
        min_index=i
       
        for j in range(i+1,len(arr)):
            if arr[min_index] > arr[j]:
                min_index = j
                
            #arr[i], arr[min_index] = arr[min_index], arr[i]
                temp= arr[min_index]
                arr[min_index]=arr[i]
                arr[i]=temp 
    return arr
        
arr=[2,3,5,1,0,6,4]
print(selectionSort(arr))


print("--- %s seconds ---" % (time.time() - start_time))
