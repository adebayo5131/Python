##def reverse(s):
##    return s[::-1]
##
##def isPalindrome(s):
##    checkRev = reverse(s)
##
##    if s == checkRev:
##        return True
##    else:
##        return False
##
##    return null
##
##word= 'aaa'  
##answer = isPalindrome(word)
##if(answer == True):
##    print('yes')
##else:
##    print('no')


check = 'noa'
x= ""

for i in check: 
    x = i + x
    if (check==x): 
        print("YES")
    print(x)
