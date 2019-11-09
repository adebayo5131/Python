import pprint
dic = {} 
  
def countFreq(a): 
    global dic 

  
    for i in a:
        dic.setdefault(i,0)
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
    

def query(): 
    for i in dic:
        print(str(i) + ' heads' +' ' + str(dic[i])+ ' times')

arr = [6, 3, 4, 6, 5, 4, 5, 8, 4, 3, 3, 6, 4, 2, 6, 5, 5, 4, 4, 6, 5, 7,
       5, 4, 7, 4, 2, 6, 3, 5, 6, 8, 5, 5, 3, 8, 5, 3, 7, 4, 8, 6, 7, 8,
       7, 5, 5, 5, 5, 3, 6, 5, 3, 7, 4, 2, 6, 2, 5, 4, 4, 5, 6, 7, 5, 3,
       9, 6, 4, 3, 5, 2, 4, 5, 7, 6, 6, 7, 6, 3, 9, 5, 5, 5, 4, 5, 4, 3,
       5, 6, 2, 5, 3, 7, 5, 6, 2, 4, 4, 5]

countFreq(arr)
query()

print(' ')

pprint.pprint(dic)




