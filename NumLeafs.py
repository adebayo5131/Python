class Node:
    def __init__(self,data):
        self.value = data
        self.left = None
        self.right = None

def getNumOfleaf(node):
    if node is None:
        return 0
    if(node.left is None and node.right is None):
        return 1
    else:
        return getNumOfleaf(node.left) + getNumOfleaf(node.right)

root = Node(1) 
root.left = Node(2) 
root.right = Node(3) 
root.left.left = Node(4) 
root.left.right = Node(5)

print(getNumOfleaf(root))
