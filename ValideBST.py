class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Average Case: O(logn) time || O(1) space
    # Worse Case is O(n) time || O(1) space
    def insert(self, key):
        if self.value > key:
            if self.left is None:
                self.left = BST(key)
            else:
                self.left.insert(key)
        else:
            if self.right is None:
                self.right = BST(key)
            else:
                self.right.insert(key)
        return self


def validateBst(tree):
    return helper(tree, float("-inf"), float("inf"))


def helper(tree, minValue, maxValue):
    if tree is None:
        return True
    if tree.value < minValue or tree.value >= maxValue:
        return False
    leftisValid = helper(tree.left, minValue, tree.value)
    return leftisValid and helper(tree.right, tree.value, maxValue)


test1 = (
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

print(validateBst(test1))
