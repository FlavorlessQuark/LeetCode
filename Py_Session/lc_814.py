# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def traverse(node):
            isValid = node.val
            
            if (node.left):
                if (traverse(node.left)):
                    isValid += 1
                else:
                    node.left = None
            if (node.right):
                if (traverse(node.right)):
                    isValid += 1
                else:
                    node.right = None
            return isValid
        
        if (not traverse(root)):
            root = None
        return root
