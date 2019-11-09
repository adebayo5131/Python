print('I\'m 5 years old.\n\tHow old are you?\n\t\tDo you want to ask me a question?')

word = 'Adebayo5131'

print(word.isalpha())
print(word.isalnum())
print(word.isdecimal())
print(word.istitle())
print(word.isupper())
print(word.islower())


word2 = 'the begining of a new world'
print(word2.title()+'\n')

#Join method
joinMethod ='.'.join(['cats', 'dogs' ,'rats'])
print(joinMethod)
print()
joinMethod =','.join(['cats', 'dogs' ,'rats'])
print(joinMethod)
print()
joinMethod ='\n\n'.join(['cats', 'dogs' ,'rats'])
print(joinMethod+'\n')

splitMethod = 'This is how split method works'
print(splitMethod.split())

#split on a particular string
splitMethod = 'This is how split method works'
print(splitMethod.split('i'))

#rjust() and ljust()

string ='Hello'
print(string.rjust(10) +'\n')

string ='Hello'
print(string.ljust(10) +'\n')

string ='Hello'
print(string.rjust(15,'*') +'\n')

string ='Hello'

print(string.ljust(15,'~') +'\n')

string ='Hello'
print(string.center(10,'*') +'\n')

#strip removes white spaces

word3 =" Adebayo Ajagunna"
neword = word3
print(word3.center(20,'*'))
print(neword.strip())

#lstrip() rstrip()

print('x     '.strip())

print('Adebayo Edward AjagunnA'.strip('Ae'))

#Repalce

wordToReplace ='Adebayo Ajagunna'
print('\n'+wordToReplace.replace('a', 'o'))
