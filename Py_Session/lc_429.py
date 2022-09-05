"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        lst = []
        vals = []
        if(root):
            lst.append(root)
        i = 0
        print(lst)
        while (i < len(lst)):
            length = len(lst)
            level = []
            while (i < length):
                level.append(lst[i].val)
                for child in lst[i].children:
                    lst.append(child)
                i += 1
            vals.append(level)
        return vals
