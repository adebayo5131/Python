name = 'Adebayo'
age =20
if name == 'cat':
    print('yes')
elif age == 20 and name == 'Adebayo':
    print('yes you are right')
else:
    print('They do not eqaul each other')
   
i = 0
sum = 0
number = int(input('Enter a number to sum: '))
while i < number:
    i = i + 1
    sum = i + sum
print(sum)



spam = 0
while spam < 5:
    spam = spam + 1
    if spam == 3:
        #ignores when spam ==3
        continue
    print('spam is ' + str(spam))
        
add = 0
for i in range(11):
    add = add +i
print(add)
     
