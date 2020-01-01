def strWithout3a3b(A, B):
    """
    :type A: int
    :type B: int
    :rtype: str
    """

    string = ""
    length = A+B
    if A > B:
        prefix = 'b'
    else:
        prefix = 'a'

    while len(string) < length:
        if prefix == 'a':
            if B > A+1:
                string += 'bb'
                B -= 2
            else:
                string += 'b'
                B -= 1
            prefix = 'b'
        else:
            if A > B+1:
                string += 'aa'
                A -= 2
            else:
                string += 'a'
                A -= 1
            prefix = 'a'
    return string


print(strWithout3a3b(6, 6))
