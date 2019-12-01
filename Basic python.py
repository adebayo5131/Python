greet = 'Hello my name is'

for i in enumerate(greet):
    print(i)
print('\n')

for j in enumerate(greet[0:5]):
    print(j)

#List Comprehension
list = [1,2,3,4,5]

print('\n')

print([i**2 for i in list])


items = [['Bayo',20],['shaina',10]]

print(items[1][1]* 2)

print('\n')

#Lambda(), Map() and Filter()
for i in map(lambda x: x*2, list):
    print(i)
    
print('\n')

for i in filter(lambda x: x>3,list):
    print(i)

print('\n')

word = str.split( 'Here is how to use the split')
print(sorted(word,key=len))
print('\n')

sl = ['A','B','a','C', 'c']
sl.sort(key=str.lower)
print(sl)
print('\n')

sl.sort()
print(sl)

