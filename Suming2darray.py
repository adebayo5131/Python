def find_Sum(n):
    total = 0
    i = 0

    #check using
##    for i in range(len(n)):
##        total += sum((n[i]))
##    return total

    for i in range(len(n)):
        for j in range(len(n[i])):
            total += n[i][j]
    return total
n = [[1,1,1,1,1],
     [2,2,2,2,2],
     [3,3,3,3,3]]
print(find_Sum(n))
