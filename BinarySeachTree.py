class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


def insertNode(root, node):

    if root is None:
        root = node
    else:
        if root.val < node.val:
            if root.right is None:
                root.right = node
            else:
                insertNode(root.right, node)
        else:
            if root.left is None:
                root.left = node
            else:
                insertNode(root.left, node)


def inOrder(root):
    if root:
        inOrder(root.left)
        print(root.val)
        inOrder(root.right)


r = Node(50)
insertNode(r, Node(30))
insertNode(r, Node(20))
insertNode(r, Node(40))
insertNode(r, Node(70))
insertNode(r, Node(60))
insertNode(r, Node(80))

print(inOrder(r))
