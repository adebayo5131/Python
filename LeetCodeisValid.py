class Solution(object):
    def isValid(self, string):
        
        dictionary = { ")": "(",
                       "}": "{",
                        "]": "["
                      }

        stack = []
     
        for openingCharacter in string:
            if openingCharacter in dictionary:
                if stack == []:
                    lastIn = "!"
                else:
                      lastIn= stack.pop() 
                        
                if dictionary[openingCharacter] != lastIn:
                    return False
            else:
                stack.append(openingCharacter)
        return not stack
vst = Solution()
exp = "[]"

print(vst.isValid(exp))
