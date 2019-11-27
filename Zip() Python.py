
# initializing list of players. 
name= [ "Ade", "Shaina"] 
  
# initializing their scores 
grade = [100, 15] 
  
# printing players and scores. 
for i, j in zip(name,grade ):
    print ("Name :  %s     Grade: %d" %(i, j))


num1 = [1,2,3,4,5,6]   
num2 = [2,3,4,5,6,6] 

sum = []
in1array = 0

totalSum = 0
for i, j in zip(num1, num2):

    in1array = i+j
    sum.append(i+j)
    
for i in range(len(sum)):
    totalSum += sum[i]

print(in1array)
print(sum)
print(totalSum)
