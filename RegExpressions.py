import re

lyric = '12 drummer drumming, 11 piper pipping, 10 lordsa leaping, 9 ladies dancing, 8 maids are milking,\
7 swans are swimming, 6 geese a laying, 5 golden rings, 4 calling birds, 3 french hens, 2 turtle doves, and 1 partidge in a pear tree '

lyricRegex = re.compile(r'\d+\s\w+')
mo= lyricRegex.findall(lyric)
print(mo,'\n')

message='Call me on 222-332-3333 or try 444-111-3333'
phoneNumber = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
po = phoneNumber.findall(message)
print(po, '\n')

vowels = 'My name is james brandon messi oo'
vowelRegex = re.compile(r'[aeiouAEIOU]')
vo = vowelRegex.findall(vowels)
print(vo, '\n')


notvowels = re.compile(r'[^aeiouAEIOU]')
no = notvowels.findall(vowels)
print(no,'\n')

notvowels = re.compile(r'[aeiouAEIOU] {2}')
bo = notvowels.findall(vowels)
print(bo, '\n')

notvowels = re.compile(r'[^aeiouAEIOU]')
no = notvowels.findall(vowels)
print(no, '\n')


regexfl = re.compile(r'First Name: (.*) Last Name: (.*)')
fl = regexfl.findall('First Name: Adebayo Last Name: Ajagunna')
print(fl,'\n')

atRegex = re.compile(r'.{1,2}at')
lu = atRegex.findall('The cat in the hat sat on the flat mat at')
print(lu, '\n')


#Non-Greedy and not greedy search
check = '<This is a greedy search> here you go>'
non_greedy = re.compile(r'<(.*?)>')
ng = non_greedy.findall(check)
print(ng ,'\n')

#Greedy Search
greedy = re.compile(r'<(.*)>')
gg = greedy.findall(check)
print(gg ,'\n')

