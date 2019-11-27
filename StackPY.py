Stack = []


StackSize = 5

def showStack():
    print("Elemet in stack are:")
    for i in Stack:
        print(i)

  
def Push(Value):
 if len(Stack) < StackSize:
  Stack.append(Value)
 else:
  print("Stack is full!")

  
def Pop():
    popped = 0
    if len(Stack) > 0:
        print("Remove and display Value")
        popped = Stack.pop()
        print(popped)
    else:
        print("Stack is empty.")


print("Driver")
Push(1)
Push(2)
Push(3)
showStack()

Pop()
showStack()
