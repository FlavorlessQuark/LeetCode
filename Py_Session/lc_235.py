class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if (not root):
            return
        if (q.val < root.val and p.val < root.val):
            return self.lowestCommonAncestor(root.left, p, q)
        if (q.val > root.val and p.val > root.val):
            return self.lowestCommonAncestor(root.right, p, q)

        return root
