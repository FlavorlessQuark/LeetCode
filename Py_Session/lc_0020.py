class Solution(object):
    def isValid(self, s):
        while ("()" in s or "[]" in s or '{}' in s):
            s = s.replace("()", "").replace('[]', "").replace('{}', "")
        return len(s) == 0

    def isValid(self, s: str) -> bool:
        dic = {
            ')' : '(',
            ']' : '[',
            '}' : '{'
        }

        stack = []

        for x in s:
            if (x not in dic):
                stack.append(x)
            else:
                # print(stack, x)
                if (len(stack) == 0 or dic[x] != stack[-1]):
                    return False
                else:
                    stack.pop()
        return len(stack) == 0
