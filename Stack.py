class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self.size = 0
    
    def push(self, data):
        node = Node(data)
        
        if self.top:
            node.next = self.top
            self.top = node
        else:
            self.top = node
        self.size+=1
            
    def pop(self):
        if self.top:
            data = self.top.data
            self.size-=1
            if self.top.next:
                self.top = self.top.next
            else:
                self.next = None
            return data
        else:
            return None
    def peek(self):
        if self.top:
            return self.top.data
        else:
            return None
            
stack = Stack()

stack.push(6)
stack.push(4)
stack.push(3)
stack.push(2)

print(stack.pop())

print(stack.peek())