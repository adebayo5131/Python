import re

message='Call me on 222-332-3333 '

phoneNumber = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')

#Matched Object
mo = phoneNumber.search(message)

#search by groups, area code
print(mo.group(1) +'\n')

#Escape character looking for area code with parenthesis
text='Call me on (222)-332-3333 '
phoneNum = re.compile(r'\(\d\d\d\)-(\d\d\d-\d\d\d\d)')

#Matched Object
mO = phoneNum.search(text)
print(mO.group() +'\n')

#Searching for words with patterns using regular expressions and pipe |

word='Batman used a Batmobile to trap a Batbat in Batcopter'
wordReg= re.compile(r'Bat(mobile|man|corper|bat)')

#Matched Object
wo = wordReg.findall(word)
print(wo)


