
def findMissing(first,second):
    # convert list to set and subtract
    #use aseert as a condition to determine the expected output
    #Convert back to a list
    
    if (len(first)> len(second)):
        missing = set(first) - set(second)
        print(missing)
        assert(len(missing)) ==1
        return list(missing)
    else:
        missing = set(second) - set(first)
        print(missing)
        assert(len(missing)) == 1
        return list(missing)



print(findMissing([1,2,3,5],[1,2,3,4,5]))
