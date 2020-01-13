def search_entry_equal_to_its_index(array):
    left = 0
    right = len(array)

    while left <= right:
        mid = (left + right) // 2
        difference = array[mid] - mid

        if difference == 0:
            return mid
        if difference > 0:
            right = mid - 1
        else:
            left = mid + 1
    return - 1


print(search_entry_equal_to_its_index([-2, 0, 2, 4, 6, 7, 9]))
