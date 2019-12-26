def minimumRemoval(string):
    dictionary = { ")": "(",
               "}": "{",
               "]": "["
            }

    stack = []
    count = 0
    for openingCharacter in string:
        if openingCharacter in dictionary:
            if stack == []:
                lastIn = "!"
            else:
                  lastIn= stack.pop()   
            if dictionary[openingCharacter] != lastIn:
                count+=1
        else:
            stack.append(openingCharacter)
    return count

s = "()())}()"
print(minimumRemoval(s))