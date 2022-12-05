class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        arr = [root.left, root.right]
        i = 0
        while(i < len(arr)):
            l = arr[i]
            r = arr[i + 1]
            lval = None if l == None else l.val
            rval = None if r == None else r.val
            arr[i] = lval
            arr[i + 1] = rval

            if (rval != lval):
                # print("NOPE",arr)
                return False
            if (lval != None):
                # print(arr)
                arr.extend([l.left, r.right, l.right, r.left])

        # print(arr)
            i += 2
        return True
