import re

lyric = '12 drummer drumming, 11 piper pipping, 10 lordsa leaping, 9 ladies dancing, 8 maids are milking,\
7 swans are swimming, 6 geese a laying, 5 golden rings, 4 calling birds, 3 french hens, 2 turtle doves, and 1 partidge in a pear tree '

lyricRegex = re.compile(r'\d+\s\w+')
mo= lyricRegex.findall(lyric)
print(mo)

message='Call me on 222-332-3333 or try 444-111-3333'
phoneNumber = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
po = phoneNumber.findall(message)
print(po)

vowels = 'My name is james brandon messi'
vowelRegex = re.compile(r'[aeiouAEIOU]')
vo = vowelRegex.findall(vowels)
print(vo)


notvowels = re.compile(r'[^aeiouAEIOU]')
no = notvowels.findall(vowels)
print(no)

notvowels = re.compile(r'[^aeiouAEIOU] {2}')
no = notvowels.findall(vowels)
print(no)
