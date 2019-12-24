# We can do a BFS trevasal using a queue to treverse each level interatively
# and swapping the levels as we go


class BST:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

    def insert(self, newKey):
        if self.value > newKey:
            if self.left is None:
                self.left = BST(newKey)
            else:
                self.left.insert(newKey)
        else:
            if self.right is None:
                self.right = BST(newKey)
            else:
                self.right.insert(newKey)
        return self

# O(n) time || O(d) space


def invertBinaryTreeWithoutQueue(tree):
    if tree is None:
        return None
    tree.left, tree.right = tree.right, tree.left
    invertBinaryTreeWithoutQueue(tree.left)
    invertBinaryTreeWithoutQueue(tree.right)

# O(n) time || O(n) space


def invertBinaryTree(tree):
    queue = [tree]

    while len(queue):
        current = queue.pop(0)
        if current is None:
            continue
        swapper(current)
        invertBinaryTree(tree.left)
        invertBinaryTree(tree.right)


def swapper(tree):
    tree.left, tree.right = tree.right, tree.left

# Average O(n) time || O(n) space


def inOrderTraverse(tree, array):
    if tree:
        inOrderTraverse(tree.left, array)
        array.append(tree.value)
        inOrderTraverse(tree.right, array)
    return array


test = (
    BST(10)
    .insert(5)
    .insert(15)
    .insert(5)
    .insert(2)
    .insert(1)
    .insert(22)
    .insert(13)
    .insert(14)
)

array = []
array2 = []

invertBinaryTreeWithoutQueue(test)
print("inOrder Treversal without queue", inOrderTraverse(test, array), "\n")
invertBinaryTree(test)
print("inOrder Treversal with queue", inOrderTraverse(test, array2))
