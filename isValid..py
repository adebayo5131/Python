# Check if a string has a valid paranthesis


def isValid(string):

    dictionary = {")": "(",
                  "}": "{",
                  "]": "["
                  }

    stack = []

    for opening in string:
        if opening in dictionary:
            if stack == []:
                last = "?"
            else:
                last = stack.pop()
            if dictionary[opening] != last:
                return False
        else:
            stack.append(opening)
    return not stack


n = "()"
print(isValid(n))
