class Node:
    def __init__ (self, data=None):
        self.data = data
        self.next = None
        
class llist:
    def __init__ (self):
        self.head = None
        self.size = 0
        
    
    def append (self, data = None):
        node = Node(data)
        
        if self.head is None:
            self.head = node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = node
    
    def iter(self):
        
        current = self.head
        while current:
            self.size+=1
            print(current.data)
            current = current.next
    
    def removeNode(self, data):
        current = self.head
        prev = self.head
        while current:
            if current.data == data:
                if current == self.head:
                    self.head = current.next
                else:
                    prev.next = current.next
                    self.size-=1
            prev = current
            current = current.next
            
        
            
    def reverseList(self):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        current = self.head
        previous = None
        while  current:
            nxt =  current.next
            current.next = previous
            previous =  current
            current = nxt
        self.head = previous       
     
     
        
            
        
link = llist()
    
link.append(5)
link.append(6)
link.append(4)

link.reverseList()
link.iter()
