# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def sameTree(self, treeA, treeB):
        if not treeA and not treeB:
            return True

        if not treeA or not treeB:
            return False

        if sameTree(treeA.left, tree.left) and sameTree(treeA.right, treeB.right):
            return treeA.val == treeB.val


print(TreeNode.sameTree([1, 2], [1, None, 2]))
