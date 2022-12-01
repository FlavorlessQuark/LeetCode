class Solution:
    m = 0
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def diameter(root, depth):
            if not root:
                return depth
            
            l = diameter(root.left, depth)
            r = diameter(root.right, depth)

            self.m = max(self.m, l + r)
            return max(l, r) + 1
        diameter(root, 0)
        return self.m
