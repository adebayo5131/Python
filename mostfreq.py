def mostfrequency(array):
    if not array:
        return 
    
    freq = {}
    
    for i in array:
        if i in freq:
            freq[i] +=1
        else:
            freq[i] = 1
    
    mostFreq= prev =float("-inf")
    most = 0
    for i in freq:
        mostFreq = max(freq[i], mostFreq)
        if freq[i] > prev:
            most = i
            prev = freq[i]
    return most 

array = [6,1,1,2,1,8,9,6,6,6,6]
print(mostfrequency(array))