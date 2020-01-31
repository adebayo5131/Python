from collections import deque


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def insert(self, key):
        if not self:
            self = key
        elif self.value > key:
            if self.left is None:
                self.left = Node(key)
            else:
                self.left.insert(key)
        else:
            if self.right is None:
                self.right = Node(key)
            else:
                self.right.insert(key)
        return self


def print_level_order(root):
    queue = deque([root])
    levelOrder = []

    while queue:
        current = queue.popleft()
        levelOrder.append(current.value)
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
    return levelOrder


test1 = (Node(10).insert(5).insert(15).insert(
    5).insert(2).insert(14).insert(22))

print(print_level_order(test1))
