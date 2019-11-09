list = ['cats', 'dogs', 'rats', 'elephant', 'donkey']


list.append('Lizard')
print(list)
print(' ')

list.insert(3, 'ram')
print(list)
print(' ')

list.append('cats')
list.append('dogs')
list.append('rats')
print(list)
print(' ')

list.remove('dogs')
print(list)
print(' ')

del list[1]
print(list)
print(' ')

print(list.index('elephant'))
print(' ')

print(len(list))
print(' ')

list = ['cats', 'dogs', 'rats', 'elephant']
a = list
print(a)

animals = ['cats', 'dogs', 'rats', 'elephant', 'donkey']

for i in range(len(animals)):
    print('Index ' + str(i) + ' contains ' + animals[i])



numbers = [1,3,4,5,6,7,2,1,4,5,6,8,9]
numbers.sort()
print(numbers)

numbers.sort(reverse=True)
print(numbers)

numbers = [1,3,4,5,6,7,2,1,4,5,6,8,9]
print(" " )



