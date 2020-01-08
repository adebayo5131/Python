def hasPathSum(self, root, sum):
    """
    :type root: TreeNode
    :type sum: int
    :rtype: bool
    """
    #The time complexity and space complexity O(n) O(h), respectively.
    if not root:
        return False
    if not root.left and not root.right and root.val == sum:
        return True
    sum = sum- root.val
    return self.hasPathSum(root.left, sum) or self.hasPathSum(root.right, sum)

    # if not root:
    #     return False
    # stack = [(root, root.val)]
    # while stack:
    #     curr, val = stack.pop()
    #     if not curr.left and not curr.right:
    #         if val == sum:
    #             return True
    #     if curr.right:
    #         stack.append((curr.right, val+curr.right.val))
    #     if curr.left:
    #         stack.append((curr.left, val+curr.left.val))
    # return False