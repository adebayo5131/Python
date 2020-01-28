def setZeroes(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: None Do not return anything, modify matrix in-place instead.
    """
    row = len(matrix)
    col = len(matrix[0])
    indexrow = set()
    indexcol = set()

    for i in range(row):
        for j in range(col):
            if matrix[i][j] == 0:
                indexrow.add(i)
                indexcol.add(j)

    for i in range(row):
        for j in range(col):
            if i in indexrow or j in indexcol:
                matrix[i][j] = 0
    return matrix


matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
print(setZeroes(matrix))
