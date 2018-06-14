#input in python
"""
print("how old are you?")



x= input()

print(x)
"""

thislist = list(("apple", "banana", "cherry"))

#add to list
thislist.append("damson")
#remove from list
thislist.remove("cherry")
print(thislist)

#Set in Python

thisset ={"apple", "mango", "banana"}
thisset.add("grapes")
thisset.remove("banana")

print (thisset)

#Dictionary are unordered and changeable
thisdict =	{
  "apple": "green",
  "banana": "yellow",
  "cherry": "red"
}
thisdict["apple"] = "red"

#adding an item
thisdict["ade"] ="blue"
#removing an item
del(thisdict["banana"])

print(thisdict)

#using dit to make a dictionary
thisdict =	dict(apple="green", banana="yellow", cherry="red")
# note that keywords are not string literals
# note the use of equals rather than colon for the assignment
print(thisdict)


