def longestPalindromicSubstring(string):
    checker = ""
    for i in range(len(string)):
        for j in range(i, len(string)):
            subString = string[i:j+1]
            if len(subString) > len(checker) and isPalindrome(subString):
                checker = subString
    return checker
    
def isPalindrome(s):
    left = 0
    right = len(s)-1
    
    while left < right:
        if s[left] != s[right]:
            return False
        left+=1
        right-=1
    return True
            

# def isPalindrome(s):
#     w = ""
#     for i in s:
#         w = i + w
#         if w == s:
#             return True

#     return False


print(longestPalindromicSubstring("it's Honeynoon"))
