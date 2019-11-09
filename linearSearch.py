import time
start_time = time.time()

def linearSearch(arr,v):

    for i in range(len(arr)):
        if arr[i] == v:
            return i
    return None
    

arr=[2,3,5,1,0,6,4]
print(linearSearch(arr,6))

print("--- %s seconds ---" % (time.time() - start_time))
