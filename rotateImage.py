def rotate(matrix):
    """
    :type A: List[List[int]]
    :rtype: List[List[int]]
    """
    #Yields a transpose and we reverse the transpose to yield a rotate
    for i in range(len(matrix)):
        for j in range(i, len(matrix)):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for i in range(len(matrix)):
        matrix[i].reverse()
    return matrix


route = [[10, 2, 3], [4, 5, 6], [7, 8, 9]]
print(rotate(route))
