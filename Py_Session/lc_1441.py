class Solution(object):
    def buildArray(self, target, n):
        stack = []

        i = 0
        x = 1
        while (i < len(target)):
            # print(x)
            if (x == target[i]):
                stack.append("Push")
                i += 1
            else :
                stack.append("Push")
                stack.append("Pop")
            x += 1
        return stack
