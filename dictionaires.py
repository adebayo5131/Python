import pprint
message = ' This is the first time  I will be using a dictionary, I am a new to python.'

dic={}

def countCha(message):
    global dic
    
    for i in message:
        dic.setdefault(i,0)
        dic[i] = dic[i]+1

countCha(message)
pprint.pprint(dic)
