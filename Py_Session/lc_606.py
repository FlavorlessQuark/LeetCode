# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, node: Optional[TreeNode]) -> str:
        
        # def buildStr(node) -> str:
        string = str(node.val)
        if (not node.left and not node.right):
            return string
#             L & !R = _  L & R = () !L & R = ()

        if (node.left):
            string += "(" + self.tree2str(node.left) + ")"
        else :
            string += "()"
        if (node.right):
            string += "(" + self.tree2str(node.right) + ")"
        return string
        
        # buildStr(root
        # print(string)
        # return string
            
