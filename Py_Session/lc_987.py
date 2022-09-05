# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        positions = {}
        def traverse(node, col, row):
            if col not in positions:
                positions[col] = {}
            if row not in positions[col]:
                positions[col][row] = []
            positions[col][row].append(node.val)
            
            if (node.left):
                traverse(node.left, col - 1, row + 1)
            if (node.right):
                traverse(node.right, col + 1, row + 1)
        traverse(root, 0, 0)
        keys = sorted(positions)
        traversal = []
        for key in keys:
            values = []
            row = positions[key]
            for val in sorted(row):
                row[val].sort()
                for item in row[val]:
                    values.append(item)
            traversal.append(values)
        # print(positions)
        # print(traversal)
        return traversal
        # print(sorted(positions))
            
