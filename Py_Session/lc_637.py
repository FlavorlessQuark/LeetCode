# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        avgs = []
        nodes = []

        i = 0
        nodes.append(root)
        while (i < len(nodes)):
            currentSize = len(nodes)

            avg = 0
            x = i
            while x < currentSize:
                if (nodes[x].left):
                    nodes.append(nodes[x].left)
                if (nodes[x].right):
                    nodes.append(nodes[x].right)
                avg += nodes[x].val
                x += 1

            avg /= (x - i)
            avgs.append(avg)
            i = x

        return(avgs)
