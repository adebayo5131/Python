def reverse(x):
    result = 0
    remaining = abs(x)
    while remaining:
        result = result * 10 + remaining % 10
        remaining //= 10

    minX = -2**31
    maxX = 2 ** 31 - 1

    if result < maxX and result > minX:
        return -result if x < 0 else result
    else:
        return 0


print(reverse(-5678))
