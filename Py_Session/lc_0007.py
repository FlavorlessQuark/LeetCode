class Solution:
    def reverse(self, x: int) -> int:
        if x > 0:
            n = int(str(x)[::-1])
        else:
            n = int(str(abs(x))[::-1]) * - 1

        if -2147483648 <= n <= 2147483647:
            return n
        return 0
