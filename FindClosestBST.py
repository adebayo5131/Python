
# Average is O(logn) and O(1) space where is the number of nodes in our tree
# This is because we are eliminating half of the tree
# Worse Case == O(n) time || O(n) space
#


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Average Case: O(logn) time || O(1) space
    # Worse Case is O(n) time || O(1) space
    def insert(self, key):
        currentNode = self
        while self:
            if currentNode.value > key:
                if currentNode.left is None:
                    currentNode.left = BST(key)
                    break
                else:
                    currentNode = currentNode.left
            else:
                if currentNode.right is None:
                    currentNode.right = BST(key)
                    break
                else:
                    currentNode = currentNode.right
        return self

    # Average Case: O(logn) time || O(1) space
    # Worse Case is O(n) time || O(1) space
    def contains(self, keyToCheck):
        currentNode = self
        while currentNode is not None:
            if currentNode.value > keyToCheck:
                currentNode = currentNode.left
            elif currentNode.value < keyToCheck:
                currentNode = currentNode.right
            else:
                return True
        return False

    def getMinValue(self):
        currentNode = self
        while currentNode.left is not None:
            currentNode = currentNode.left
        return currentNode.value


# Average is O(logn) and O(1) space where is the number of nodes in our tree
# This is because we are eliminating half of the tree
# Worse Case == O(n) time || O(n) space


    def findClosestValueInBst(self, target):
        closest = float("inf")
        currentNode = self
        while currentNode is not None:
            if abs(closest - target) > abs(currentNode.value-target):
                closest = currentNode.value
            if currentNode.value > target:
                currentNode = currentNode.left
            elif currentNode.value < target:
                currentNode = currentNode.right
            else:
                break
        return closest

# O(n) Time || O(n) space


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


# Average O(n) time | | O(n) space


def preOrderTraverse(tree, array):
    if tree:
        array.append(tree.value)
        preOrderTraverse(tree.left, array)
        preOrderTraverse(tree.right, array)
    return array

# Average O(n) time || O(n) space


def postOrderTraverse(tree, array):
    if tree:
        postOrderTraverse(tree.left, array)
        postOrderTraverse(tree.right, array)
        array.append(tree.value)
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
array3 = []
array4 = []


print(test.contains(1), "\n")
print(test.getMinValue(), "\n")
print("InOrder: ", inOrderTraverse(test, array), "\n")
print("PreOrder ", preOrderTraverse(test, array2), "\n")
print("PostOrder: ", postOrderTraverse(test, array3), "\n")
print(test.findClosestValueInBst(12), "\n")
invertBinaryTree(test)
print("Invert a Binary tree inorder Traversal", inOrderTraverse(test, array4))
