class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, key):
        currentNode = self
        while True:
            if currentNode.value > key:
                if currentNode.left is None:
                    currentNode.left = BinaryTree(key)
                    break
                else:
                    currentNode = currentNode.left
            else:
                if currentNode.right is None:
                    currentNode.right = BinaryTree(key)
                    break
                else:
                    currentNode = currentNode.right
        return self

    # O(n) time and O(n) space where n is the number of nodes in the Binary Tree
    def branchSums(self):
        sums = []
        presentSum = 0
        calculateleafs(self, presentSum, sums)
        return sums


def calculateleafs(self, presentsum, sums):

    # Check root node
    if self is None:
        return None

    newSum = presentsum + self.value

    if self.left is None and self.right is None:
        # return the root in an array
        return sums.append(newSum)

    calculateleafs(self.left, newSum, sums)
    calculateleafs(self.right, newSum, sums)


test = (
    BinaryTree(10)
    .insert(5)
    .insert(15)
    .insert(5)
    .insert(2)
    .insert(1)
    .insert(22)
    .insert(13)
    .insert(14)
)


print(test.branchSums())
