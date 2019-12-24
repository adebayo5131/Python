def longestPalindromicSubstring(string):
    checker = ""
    string = string.replace(' ', '')
    for i in range(len(string)):
        for j in range(i, len(string)):
            subString = string[i:j+1]
            if len(subString) > len(checker) and isPalindrome(subString):
                checker = subString
    return checker


def isPalindrome(s):
    w = ""
    for i in s:
        w = i + w
    if w == s:
        return True
    else:
        return False


print(longestPalindromicSubstring("it's Honeynoon"))
