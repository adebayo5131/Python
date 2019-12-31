
def maxDistToClosest(seats):

    maxDist = seats.index(1)
    currentDist = 0
    for i in range(len(seats)):
        if seats[i] == 0:
            currentDist += 1
        else:
            maxDist = max(maxDist, (currentDist+1)//2)
            currentDist = 0

    return max(maxDist, currentDist)


arr = [1, 0, 0, 0, 1, 0, 1]
test2 = [1, 0, 0, 0]
print(maxDistToClosest(arr))
