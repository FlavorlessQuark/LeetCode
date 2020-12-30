def center(start, end , s):
        while end < len(s) and start >= 0 and s[start] == s[end]:
                end +=1
                start -= 1
        return (end - start - 1)

class Solution:

    def longestPalindrome(self, s: str) -> str:

        if not s:
            return ""

        result = [0, 0]
        for i in range(len(s)):
            even = center(i , i + 1, s)
            odd = center(i, i, s)
            m = max(even, odd)
            if result[0] < m:
                result[0] = m
                result[1] = i
        return s[result[1] - ((result[0] - 1)// 2):result[1] + (result[0] // 2) + 1]

