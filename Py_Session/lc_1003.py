class Solution(object):
    def isValid(self, s):
        while "abc" in s:
            s = s.replace("abc", "")
        return s == ""
