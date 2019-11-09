
list = [2, 5, 3, 4, 1]

for index in range(1, len(list)):

            # value of index are all the values except the first
    value_of_index = list[index]
    i = index - 1  # i is at the left of 5 which is 2

    while i >= 0:
        if value_of_index < list[i]:

                # shift number in slot i right of slot i +1
            list[i + 1] = list[i]
            list[i] = value_of_index  # shift number in left to the slot i
            i = i-1

        elif value_of_index > list[i]:

            list[i] = value_of_index  # shift number in left to the slot i
            i = i-1
print(list)
