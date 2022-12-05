class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        i = len(s) - 1
        j = len(t) - 1
        a = []
        b = []
        skip = 0
        while (1):
            # print(i, j)
            while (i >= 0  and (skip > 0 or s[i] == '#')):
                if (s[i] == '#'):
                    skip += 1
                else :
                    skip -= 1
                i -= 1
            skip = 0
            while (j >= 0 and (skip > 0 or t[j] == '#')):
                if (t[j] == '#'):
                    skip += 1
                else :
                    skip -= 1
                j -= 1
            skip = 0
            if (i < 0 or j < 0):
                break 
            if (s[i] != t[j]):
                return False

            a.append(s[i])
            b.append(t[j])
            i -= 1
            j -= 1
        
        print(i, j, a, b)
        return i == - 1 and j == -1

