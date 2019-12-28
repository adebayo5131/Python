from collections import deque


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


def findTarget(root, target):
    """
    :type root: TreeNode
    :type k: int
    :rtype: bool
    """

    # Using BFS
    check = set()
    queue = deque([root])
    while len(queue) > 0:
        current = queue.pop()
        if current.val in check:
            return True
        else:
            complement = target - current.val
            check.add(complement)

            if current.left is not None:
                queue.appendleft(current.left)
            if current.right is not None:
                queue.appendleft(current.right)
    return False


r = Node(50)
insertNode(r, Node(30))
insertNode(r, Node(20))
insertNode(r, Node(40))
insertNode(r, Node(70))
insertNode(r, Node(60))
insertNode(r, Node(90))
insertNode(r, Node(10))
insertNode(r, Node(5))
insertNode(r, Node(2))
insertNode(r, Node(9))

print(findTarget(r, 500))

# print(inOrder(r))
