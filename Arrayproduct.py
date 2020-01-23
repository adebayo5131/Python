def array_of_array_products(arr):

    if len(arr) == 1:
        return []

    store = []
    product = 1
    for i in range(len(arr)):
        store.append(product)
        product *= arr[i]

    product = 1
    for j in reversed(range(len(arr))):
        store[j] *= product
        product *= arr[j]
    return store

    '''
    for i in range(len(arr)):
        product = 1
        k = arr.pop(0)
        for j in range(len(arr)):
            product = product * arr[j]
            store.append(product)
            arr.append(k)
    return store
    '''


arr = [2, 7, 3, 4]
print(array_of_array_products(arr))
