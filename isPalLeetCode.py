def isPalindrome(x):
    n = str(x)
    w = ''
    for i in n:
        w = i + w
    if w == n:
        return True
    else:
        return False
x = 121
print(isPalindrome(x))
