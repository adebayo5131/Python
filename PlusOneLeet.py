def plusOne(digits):
    """
    :type digits: List[int]
    :rtype: List[int]
    """
    digits[-1] += 1
    d = len(digits)-1
    for i in range(d, 0, -1):
        if digits[i] != 10:
            break
        digits[i] = 0
        digits[i - 1] += 1

    if digits[0] == 10:
        digits[0] = 1
        digits.append(0)
    return digits

    # d = len(digits)-1
    # for i in range(d, -1, -1):
    #     if digits[i] != 9:
    #         digits[i] += 1
    #         return digits
    #     digits[i] = 0
    #     if i == 0:
    #         digits.insert(0, 1)
    #         return digits


print(plusOne([9, 9, 9]))
