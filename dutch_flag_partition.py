def dutch_flag_partition(array):

    # secondLargest = findSecondLargest(array)

    secondLargest = betterFindSecond(array)
    return sortNums(array, secondLargest)


def sortNums(array, pivot_index):
    pivot = array[pivot_index]
    smaller = 0

    for i in range(len(array)):
        if array[i] < pivot:
            array[i], array[smaller] = array[smaller], array[i]
            smaller += 1

    larger = len(array) - 1

    for i in reversed(range(len(array))):
        if array[i] < pivot:
            break
        elif array[i] > pivot:
            array[i], array[larger] = array[larger], array[i]
            larger -= 1
    return array


# Without better second largest
def betterFindSecond(array):
    minNumber = min(array)
    maxNumber = max(array)

    for i in array:
        if i != maxNumber and i != minNumber:
            return array.index(i)

# def findSecondLargest(array):

#     largest = [None, None, None]

#     for i in range(len(array)):
#         updateLargest(array[i], largest)
#         if largest[0] and largest[1] and largest[2]:
#             break

#     for i in reversed(range(len(largest)-1)):
#         if largest[i] > largest[i+1]:
#             largest[i],largest[i+1] = largest[i+1], largest[i]
#     return array.index(largest[1])


# def updateLargest(num, largest):

#     if not largest[0] or not largest[1] or not largest[2]:
#         if not largest[2]:
#             shiftUpdate(num, largest, 2)
#         elif not largest[1] and largest[2] != num:
#             shiftUpdate(num, largest, 1)
#         elif not largest[0] and (largest[1] != num and largest[2] != num):
#             shiftUpdate(num, largest, 0)


# def shiftUpdate(num, largest, position):

#     for i in range(position + 1):

#         if i == position:
#             largest[i] = num
#         else:
#             largest[i] = largest[i+1]

print(dutch_flag_partition([2, 5, 8, 2, 2, 8, 5, 8]))
