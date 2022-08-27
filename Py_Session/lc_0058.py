class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.rstrip()
        l = len(s)
        i = l - 1
        while (i >= 0):
            if (s[i] == " "):
                break
            i -= 1
        print(s)
        return (len(s) - i - 1)
