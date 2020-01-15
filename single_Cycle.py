def containsCycle(array):
    numberVisited = 0
    start = 0

    while numberVisited < len(array):
        if numberVisited > 0 and start == 0:
            return False
        numberVisited += 1
        start = getNextCycle(array, start)
    return start == 0


def getNextCycle(array, start):
    jump = array[start]
    nextvisit = (start + jump) % len(array)
    return nextvisit if nextvisit >= 0 else nextvisit + len(array)


print(containsCycle([2, 3, 1, -4, -4, 2]))
