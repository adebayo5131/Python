class Solution(object):
    def decodeAtIndex(s, k):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        if not s:
            return 0
        alphabet = number = newAlphabet = ""
        for element in s:
            if element.isalpha():
                alphabet += element
            elif element.isdigit():
                number += element
                newAlphabet += alphabet
                alphabet = newAlphabet * (int(number)-1)
                number = ''

        newList = alphabet + newAlphabet
        print(newList)
        return newList[k-1]


S = "a2345678999999999999999"
K = 1
print(Solution.decodeAtIndex(S, K))
