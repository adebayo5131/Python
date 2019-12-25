def moveElementToEnd(array, toMove):
    j = 0
    for i in range(len(array)):
        if array[i] != toMove:
            array[i], array[j] = array[j], array[i]
            j += 1
    return array


array = [5, 1, 2, 5, 5, 3, 4, 6, 7, 5, 8, 9, 10, 11, 5, 5, 12]
toMove = 5
print(moveElementToEnd(array, toMove))
