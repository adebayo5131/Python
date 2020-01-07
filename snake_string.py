def snake_string(string):
    result = []
    for i in range(1, len(string), 4):
        result.append(string[i])
    for i in range(0, len(string), 2):
        result.append(string[i])
    for i in range(3, len(string), 4):
        result.append(string[i])
    return ''.join(result)


print(snake_string("Hello World"))
