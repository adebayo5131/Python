import time
start_time = time.time()
def selectionSort(a):
    for i in range(len(a)):
        j=i+1
        for j in range(len(a)):
            if a[j] > a[i]:
                a[j], a[i] = a[i],a[j]
    return a
arr=[7, 8, 3, 11, 43, 55]
print(selectionSort(arr))


print("--- %s seconds ---" % (time.time() - start_time))
