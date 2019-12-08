class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        
    #Insert at the beginning of the linked list
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node 
        
    def append(self, new_data):  
        new_node = Node(new_data) 
        if self.head is None: 
            self.head = new_node 
            return
        
        lastNode = self.head 
        while lastNode.next is not None: 
            lastNode = lastNode.next

        #Assign LastNode the new data
        lastNode.next =  new_node

        
    def printList(self): 
        temp = self.head 
        while (temp) is not None: 
            print (temp.data)
            temp = temp.next
    
    def deleteDuplicate(self):
        
        current = self.head
        while current is not None:
            if current.next and current.next.data == current.data:
                current.next = current.next.next
            else:
                current = current.next
            
        

if __name__=='__main__':
    linkNodes = LinkedList()

    linkNodes.push(1)
    linkNodes.append(2)
    linkNodes.append(2)
    linkNodes.append(2)
    linkNodes.append(3)
    linkNodes.append(3)
    linkNodes.append(4)
    linkNodes.append(4)
    linkNodes.append(5)
    linkNodes.push(6)
    
    linkNodes.printList()


    print('Delete duplicate list')
    linkNodes.deleteDuplicate()
    
    linkNodes.printList()
            
