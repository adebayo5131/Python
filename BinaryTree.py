class Node:
    def __init__(self, val):
        self.value = val
        self.leftChild = None
        self.rightChild = None

    def insert (self, data):
        if self.value == data:
            return False
        #Data to insert is less than the root, place set it to the left side
        
        elif self.value > data:
            if self.leftChild:
                return self.leftChild.insert(data)
            else:
               self.leftChild = Node(data)
               return True
        else:
            if self.rightChild:
                return self.rightChild.insert(data)
            else:
                self.rightChild = Node(data)
                return True
            
            
    def find(self,data):
        if self.value == data:
            return True
        elif (self.value > data):
            if self.leftChild:
                return self.leftChild.find(data)
            else:
                return False
        else:
            if self.rightChild:
                return self.rightChild.find(data)
            else:
                return False

    def preOrder(self):
        if self:
            print(str(self.value))
            if self.leftChild:
                self.leftChild.preOrder()
            if self.rightChild:
                self.rightChild.preOrder()

    def postOrder(self):
        if self:
            
            if self.leftChild:
                self.leftChild.postOrder()
            if self.rightChild:
                self.rightChild.postOrder()
            print(str(self.value))
                
    def inOrder(self):
        if self:
            
            if self.leftChild:
                self.leftChild.inOrder()
            print(str(self.value))
            if self.rightChild:
                self.rightChild.inOrder()
                
    def getNumOfleaf(self):
        if self is None:
            return 0
        if(self.leftChild is None and self.rightChild is None):
            return 1
        else:
            return getNumOfleaf(self.leftChild) + getNumOfleaf(self.rightChild)
            
class Tree:

     #root node
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root:
            #If root node exist, insert data
            return self.root.insert(data)
        else:
            # if root node does not exist, create the root node
            self.root = Node(data)
            return True

    def find(self,data):
        if self.root:
            return self.root.find(data)

        else:
            return False
        
    def preOrder(self):
        print("PreOrder")
        self.root.preOrder()
        
    def postOrder(self):
        print("postOrder")
        self.root.postOrder()
        
    def inOrder(self):
        print("inOrder")
        self.root.inOrder()

    def getNumOfleaf(self):
        print("Number of leaf")
        getNumOfleaf()
        

#Instanciate tree:

bst = Tree()
bst.insert(4)
bst.insert(1)
bst.insert(2)
bst.insert(3)
bst.insert(5)
bst.insert(6)
print(bst.insert(7))
bst.preOrder()
bst.postOrder()
bst.inOrder()
print(bst.find(4))

bst.getNumOfleaf()
