class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        aq = [p]
        bq = [q]

        i = 0
        while (i < len(aq) and i < len(bq)):
            if (aq[i]):
                aq.append(aq[i].left)
                aq.append(aq[i].right)
            if (bq[i]):
                bq.append(bq[i].left)
                bq.append(bq[i].right)
            # print(i, aq, bq)
            if ((aq[i].val if aq[i] != None else None) != (bq[i].val if bq[i] != None else None)):
                return False
            i += 1
        return True
        
