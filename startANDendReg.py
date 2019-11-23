import re

beginsWithHelloRegex = re.compile(r'^Hello')
print(beginsWithHelloRegex.search('Hello there!'))

endsWithHelloRegex = re.compile(r'there!$')
print(endsWithHelloRegex.search('Hello who is there!'))

startAndEndRegex = re.compile(r'^Hello$')
print(startAndEndRegex.search('Hello'))
