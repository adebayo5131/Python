def heapify(arr, n, root):
    largest = root  # Initialize largest as root
    left = 2 * root + 1     # left = 2*i + 1
    right = 2 * root + 2     # right = 2*i + 2

    # See if left child of root exists and is
    # greater than root
    if left < n and arr[root] < arr[left]:
        largest = left

    # See if right child of root exists and is
    # greater than root
    if right < n and arr[largest] < arr[right]:
        largest = right

    # Change root, if needed
    if largest != root:
        arr[root], arr[largest] = arr[largest], arr[root]  # swap

        # Heapify the root.
        heapify(arr, n, largest)

    return arr

# The main function to sort an array of given size


def heapSort(arr):
    n = len(arr)

    # Build a maxheap.
    for root in range(n, -1, -1):
        heapify(arr, n, root)

    # One by one extract elements
    for root in range(n-1, 0, -1):
        arr[root], arr[0] = arr[0], arr[root]  # swap
        heapify(arr, root, 0)
    return arr


arr = [12, 11, 13, 5, 6, 7]
print(heapSort(arr))
