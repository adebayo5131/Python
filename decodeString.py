
def decodeString(s):
    stack = []
    alphabet, number = "", ""
    for element in s:
        if element.isalpha():
            alphabet += element
        elif element.isdigit():
            number += element
        elif element == "[":
            stack.append([alphabet, number])
            alphabet = ""
            number = ""
        else:
            [outerAlphabet, outerNumber] = stack.pop()
            alphabet = outerAlphabet + int(outerNumber) * alphabet
    return alphabet


print(decodeString('2[a2[b]c]'))
