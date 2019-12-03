total = 0
i = 0
while i < 5:
    total += i
    i += 1
print(total)


print('\n')
list = [5, 4, 3, 2, 1, -1, -2, -3, -4, -5]
total1 = 0
for i in range(len(list)):
    if list[i] > 0:
        total1 += list[i]
print(total1)

# using while loop
print('\n')

total2 = 0
j = 0
while i < len(list) and list[j] > 0:
    total2 += list[j]
    j += 1
print(total2)

print('\n')
new_list = [2, 6, 3, 4, 5, 6, -1]
i = 0
total3 = 0
while True:
    total3 += new_list[i]
    i += 1
    if new_list[i] <= 0:
        break
print(total3)
