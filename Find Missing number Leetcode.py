
def missingNumber(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    count = sum(nums)
    arrSum= 0
    for i in range(0,len(nums)+1):
        arrSum+=i
    return arrSum - count

n =[9,6,4,2,3,5,7,0,1]
print(missingNumber(n))

 
