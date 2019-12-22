def get_different_number(arr):


    #Time Complexity is O(nlogn) || space complexity O(1)
  
  arr.sort()
  
  if len(arr) == 1:
    if arr[0] == 0:
      return 1
    elif arr[0] != 0:
      return 0
    
  count = 0
  for i in range(1,len(arr)):
    count = count + 1
    
    if arr[0] != 0:
      return 0
    
    if arr[i] != count:
      return count
    
  return len(arr)
  
  pass # your code goes here

arr = [0, 1, 2, 4, 6, 8]
# [1,3,0,2]
# [100000]
#  [1,0,3,4,5]
# [0,100000]
#  [0,99999,100000]
#[0,5,4,1,3,6,2],
print(get_different_number(arr))