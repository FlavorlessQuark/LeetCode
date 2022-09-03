# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    good = 0
    def goodNodes(self, root: TreeNode) -> int:

        def dfs(node, greatest):
            if (greatest <= node.val):
                self.good += 1
                greatest = node.val

            if (node.left):
                dfs(node.left, greatest)
            if (node.right):
                dfs(node.right, greatest)

        greatest = root.val
        dfs(root, greatest)
        return self.good
