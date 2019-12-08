def Iterative_Selector(startTime , finishTime ): 
    lenghtofActivity = len(startTime)
    m = 0
    print('Index = ', m, "-->",{startTime[m],finishTime[m]}, '\n')
    for i in range(lenghtofActivity): 
        if startTime[i] >= finishTime[m]: 
            print ('Index = ', i, " --> ", sorted({startTime[i],finishTime[i]})),
            print()
            m = i 

  
startTime = [1 , 3 , 0 , 5 , 8 , 5, 6, 8, 8, 2, 12] 
finishTime = [4 , 5 , 6 , 7 , 9 , 9, 10, 11, 12, 14, 16]

print(Iterative_Selector(startTime , finishTime))

###Recursive Solution

print('\n Recurive activity Selector ')

def Recursive_Selector(startTime , finishTime, k, n):
    m = k+1

    while m <= n and startTime[m] < finishTime[k]:
        m+=1

    if m<= n:
        print('Index = ', m, "-->",{startTime[m],finishTime[m]}, '\n')
        return Recursive_Selector(startTime, finishTime,m,n)
    else:
        return None



k = 0
startTime = [1 , 3 , 0 , 5 , 8 , 5, 6, 8, 8, 2, 12] 
finishTime = [4 , 5 , 6 , 7 , 9 , 9, 10, 11, 12, 14, 16]
n = len(startTime)-1
print('Index = ', k, "-->",{startTime[k],finishTime[k]}, '\n')
print(Recursive_Selector(startTime , finishTime,k, n))
