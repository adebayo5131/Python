def first_recurring(s):
    memo = {}
    
    for i in s:
        if i in memo:
            memo[i] +=1
            if memo[i] >= 2:
                return i
        else:
            memo[i] = 1
            
    return  None
    
            


string = 'CADERTFC'
print(first_recurring(string))
