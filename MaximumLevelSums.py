# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque


class Solution(object):
    def maxLevelSum(root):
        """
        :type root: TreeNode
        :rtype: int
        """

        queue = deque([(root, 1)])
        maxLevel = float("-inf")
        maxSums = 0
        while queue:
            sums = 0
            for i in range(len(queue)):
                currentNode, level = queue.popleft()
                sums += currentNode.val
                if currentNode.left:
                    queue.append((currentNode.left, level+1))
                if currentNode.right:
                    queue.append((currentNode.right, level+1))

            if sums > maxSums:
                maxSums = sums
                maxLevel = level
        return maxLevel


print(Solution.maxLevelSum([1, 7, 0, 7, -8, 0, 0]))
