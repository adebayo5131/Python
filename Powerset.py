# we created the array n numbers of times and also we continiously doubled out
# subsets this gives us 2^n the total time complexity for the arrays is O(n*2^n) this is
# also the same for the space


def powerset(array):
    subsets = [[]]

    for elements in array:
        for i in range(len(subsets)):
            currentSubset = subsets[i]
            subsets.append(currentSubset + [elements])
    return subsets


array = [1, 2, 3]
print(powerset(array))
