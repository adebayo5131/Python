def plusOne(digits):
    """
    :type digits: List[int]
    :rtype: List[int]
    """

    d = len(digits)-1
    for i in range(d, -1, -1):
        if digits[i] != 9:
            digits[i] += 1
            return digits
        digits[i] = 0
        if i == 0:
            digits.insert(0, 1)
            return digits


print(plusOne([9]))
