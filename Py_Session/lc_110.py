class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def check(root):
            if not root:
                return 0
            
            l = check(root.left)
            r = check(root.right)

            return -1 if ((l == -1 or r == -1 ) or (abs(l - r) > 1)) else max(l, r) + 1

        return False if check(root) == -1 else True
