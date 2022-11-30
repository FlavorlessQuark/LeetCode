class Solution:
    def longestPalindrome(self, s: str) -> int:
        c = Counter(s)
        print(c)
        length = 0

        for x in c:
            length += c[x] - (1 * (length & 1) * (c[x] & 1))
        return length
