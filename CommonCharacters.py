
def commonChars(A):
    store = {}
    for char in A[0]:
        if char not in store:
            store[char] = 1
        else:
            store[char] += 1

    for char in A[1:]:
        for val in store:
            occur = char.count(val)
            store[val] = min(store[val], occur)

    returnArray = []
    for char in store:
        returnArray += [char]*store[char]
    return returnArray


A = ["bella", "label", "roller"]
[print(commonChars(A))]
