def deleteDup(A):
    j = 1
    for i in range(1, len(A)):
        if A[j-1] != A[i]:
            A[j] = A[i]
            j += 1
    return j

    # for i in range(j, len(A)):
    #     A[i] = 0

    # return A


arrayA = [1, 1, 2, 2, 3, 3, 4]
print(deleteDup(arrayA))
