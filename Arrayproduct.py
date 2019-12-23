def array_of_array_products(arr):

    if len(arr) == 1:
        return []

    store = []
    product = 1
    for i in range(len(arr)):
        store.append(product)
        product *= arr[i]

    product = 1
    for j in range(len(arr)-1, -1, -1):
        store[j] *= product
        product *= arr[j]
    return store


arr = [2, 7, 3, 4]
print(array_of_array_products(arr))
