
def searchMatrix(matrix, target):
    """
    :type matrix: List[List[int]]
    :type target: int
    :rtype: bool
    """


#             if matrix == []:
#                 return False

#             for i in range(len(matrix)):
#                 if matrix[i] == []:
#                     return False
#                 for j in range(len(matrix[i])):
#                     if matrix[i][j] == target:
#                         return True
#             return False

    if not matrix:
        return False

    col, row = len(matrix), len(matrix[0])
    i, j = 0, row - 1
    while i < col and j >= 0:
        if matrix[i][j] == target:
            return True
        if matrix[i][j] > target:
            j -= 1
        else:
            i += 1
    return False


target = 5
matrix = [
    [1,   4,  7, 11, 15],
    [2,   5,  8, 12, 19],
    [3,   6,  9, 16, 22],
    [10, 13, 14, 17, 24],
    [18, 21, 23, 26, 30]
]
print(searchMatrix(matrix, target))
