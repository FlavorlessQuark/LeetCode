# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        nodes = []
        traversal = []

        if not root:
            return []
        nodes.append(root)
        i = 0
        while (i < len(nodes)):

            current = []
            length = len(nodes)
            while (i < length):
                if (nodes[i].left):
                    nodes.append(nodes[i].left)
                if (nodes[i].right):
                    nodes.append(nodes[i].right)
                current.append(nodes[i].val)
                i += 1
            traversal.append(current)
        return traversal
