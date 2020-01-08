from collections import deque


class BST:
    def __init__(self, value=None, right=None, left=None):
        self.value = value
        self.right = right
        self.left = left

    def insert(self, key):
        if not self:
            self = key
        elif self.value > key:
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
        # currentNode = self
        # while True:
        #     if currentNode.value < key:
        #         if currentNode.right:
        #             currentNode = currentNode.right
        #         else:
        #             currentNode.right = BST(key)
        #             break
        #     else:
        #         if currentNode.left:
        #             currentNode = currentNode.left
        #         else:
        #             currentNode.left = BST(key)
        #             break
        # return self

    def inOrderTraversal(self):
        stack = []
        result = []
        while self or stack:
            if self:
                stack.append(self)
                self = self.left
            else:
                self = stack.pop()
                result.append(self.value)
                self = self.right
        return result

    def preOrder(self):
        path = [self]
        result = []

        while path:
            self = path.pop()
            if self:
                result.append(self.value)
                path += [self.right, self.left]
        return result

    def findClosetBST(self, target):
        closest = self.value
        currentNode = self
        while currentNode:
            if abs(closest - target) > abs(currentNode.value - target):
                closest = currentNode.value

            elif currentNode.value > target:
                currentNode = currentNode.left
            elif currentNode.value < target:
                currentNode = currentNode.right
            else:
                break
        return closest

    def branchSums(self):
        sums = []
        presentSum = 0

        def calculateleafs(self, presentsum, sums):
            if not self:
                return None

            newSum = presentsum + self.value

            if self.left is None and self.right is None:
                return sums.append(newSum)

            calculateleafs(self.left, newSum, sums)
            calculateleafs(self.right, newSum, sums)
            return sums

        calculateleafs(self, presentSum, sums)
        return sums


def invertBinaryTree(self):
    if not self:
        return None

    self.left, self.right = self.right, self.left
    invertBinaryTree(self.left)
    invertBinaryTree(self.right)


def validateBst(tree):
    return helper(tree, float("-inf"), float("inf"))


def helper(tree, minValue, maxValue):
    if tree is None:
        return True
    if tree.value < minValue or tree.value >= maxValue:
        return False
    leftisValid = helper(tree.left, minValue, tree.value)
    rightisValid = helper(tree.right, tree.value, maxValue)
    return leftisValid and rightisValid


def inOrder(self, array):
    if self:
        inOrder(self.left, array)
        inOrder(self.right, array)
        array.append(self.value)
    return array


def postOrder(self, array):
    if self:
        postOrder(self.left, array)
        postOrder(self.right, array)
        array.append(self.value)
    return array


def findTarget(tree, target):
    check = set()
    queue = deque([tree])

    while len(queue):
        current = queue.popleft()
        complement = target - current.value
        if complement in check:
            return True
        else:
            check.add(current.value)

        if current.left:
            queue.appendleft(current.left)
        if current.right:
            queue.appendleft(current.right)
    return False


def hasPathSum(self, root, sum):
    # The time complexity and space complexity O(n) O(h), respectively.
    if not root:
        return False
    if not root.left and not root.right and root.val == sum:
        return True
    sum = sum - root.val
    return self.hasPathSum(root.left, sum) or self.hasPathSum(root.right, sum)


test1 = (BST(10).insert(5).insert(15).insert(
    5).insert(2).insert(14).insert(22))


print('Inorder traversal recursive: ', inOrder(test1, []))
print('Inorder traversal : ', test1.inOrderTraversal())
print('Preorder traversal: ', test1.preOrder())
print('Postorder traversal: ', postOrder(test1, []))
print('ValidateBst ', validateBst(test1))
print('Branch Sum : ', test1.branchSums())
print('findclosest BST traversal: ', test1.findClosetBST(17))
print('Inverst Binary Tree traversal: ', invertBinaryTree(test1))
print('InOrder After inverting traversal: ', test1.inOrderTraversal())
print('Find target traversal: ', findTarget(test1, 36))
