#import regular expression
import re

message='Call me on 222-332-3333 or try 444-111-3333'

phoneNumber = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')

#Matched Object

mo = phoneNumber.findall(message)
print(mo)

