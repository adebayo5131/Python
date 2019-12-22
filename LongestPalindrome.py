import re
def longestPalindromicSubstring(string):
	checker = ""
	for i in range(len(string)):
		for j in range(i, len(string)):
			subString = string[i:j+1]
			if len(subString) > len(checker) and isPalindrome(subString):
				checker = subString
	return checker
				
def isPalindrome(s):
	leftIndex = 0
	rightIndex = len(s)-1
	while leftIndex < rightIndex:
		if s[leftIndex] != s[rightIndex]:
			return False
		leftIndex+=1
		rightIndex-=1
	return True

print(longestPalindromicSubstring("z234a5abbba54a32z"))