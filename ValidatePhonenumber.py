def isPhoneNumber(text):
    if len(text) != 12: #Phone number isnt 12 digits long
        return False
    for i in range(0,3): #Area code int't decimal format 
        if not text[i].isdecimal(): 
            return False
    if text[3] !='-':
        return False
    for i in range(4,7):
        if not text[i].isdecimal():
            return False
    if text[7] !='-':
        return False
    for i in range(8,12):
        if not text[i].isdecimal():
            return False
    return True

def containsPhoneNumber(message):
    foundNumber= False
    for i in range(len(message)):
        findNumber = message[i:i+12]
        if isPhoneNumber(findNumber):
            print("Phone number found "+ findNumber)
            foundNumber = True
    if not foundNumber:
        print('Could not find any number')
                        
    

message = 'You can reach me at 444-555-6666 r at 667-111-2222 tomorrow'
containsPhoneNumber(message)

