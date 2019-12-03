def iteration(low, high):
    while low <= high:
        print(low)
        low = low+1


def Recursive(low, high):
    if low <= high:
        print(low)
        Recursive(low+1, high)


print(iteration(1, 5))
print(Recursive(1, 5))
