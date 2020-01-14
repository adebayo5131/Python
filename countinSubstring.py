def countSubstrings(s):
    count = 0
    for i in range(len(s)):
        for j in range(i, len(s)):
            substring = s[i:j+1]
            if checkPalindrome(substring):
                count += 1
    return count


def checkPalindrome(s):
    check = True
    w = ''
    for i in s:
        w = i + w
        if w == s:
            return check
    return False
#     left = 0
#     right = len(s)-1


#     while left <= right:
#         if s[left] != s[right]:
#             return False
#         left+=1
#         right-=1
#     return True
print(countSubstrings("aaaabbca"))
