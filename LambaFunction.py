n = [4,3,2,1]


#Finding the max betwwen 2 numbers
maxi = lambda x,y: x if x>y else y
print(maxi(8,5),"\n")

#Map funtion

newList = lambda x:x**2
print(list(map(newList,n)), "\n")

#or
print(list(map(lambda x:x**2,n)), "\n")

#list comprehension
print([x**2 for x in n], "\n")

#Filttering a list using lambda and fillter
print(list(filter(lambda x:x>2,n)), "\n")
print(list(filter(lambda x:x<3,n)), "\n")

print(reduce(lambda x,y: x*y,n))
