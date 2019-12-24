def findDisappearedNumbers(nums):
    newArray= set(range(1,len(nums)+1))
    Original= set(nums)
    return list(newArray - Original)

nums = [4,3,2,7,8,2,3,1]
print(findDisappearedNumbers(nums))