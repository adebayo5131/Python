a = 33
b = 33

print(a+b)
if a > b:
    print("yes")
elif(a == b):
    print("They are equal")

else:
    print("no")

    print("\n")


    #while loop on python
z =1
while z <6:
    print(z)
    z += 1

    print("\n")

# #while loop with if statement
# i = 1
# while i < 6:
#   print(i)
#   if i == 3:
#     break
#   i += 1

#For loop
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x=="banana":
     break

    print(x)

    print("\n")

#skip banan
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)

  print("\n")

  # # Increment
  # # the
  # # sequence
  # with 3(default is 1):

  for x in range(2, 30, 3):
      print(x)
