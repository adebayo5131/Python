
def relativeSortArray(arr1, arr2):
 
    memo = {}
    returnValue = list()
    
    for i in  range(len(arr1)):
        if arr1[i]  in memo:
            memo[arr1[i]] +=1
        else:
            memo[arr1[i]] = 1  
    
    for i in arr2:
        if i in memo:
            returnValue.extend([i]*memo.pop(i)) 
    
    for i in memo.keys():
        returnValue.extend([i]*memo[i])
    return returnValue
        
    
    

arr1 = [2,3,1,3,2,4,6,7,9,2,19]
arr2 = [2,1,4,3,9,6]
print(relativeSortArray(arr1,arr2))
#[2,2,2,1,4,3,3,9,6,7,19]