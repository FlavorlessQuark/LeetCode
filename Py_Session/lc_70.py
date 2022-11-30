class Solution:
    def climbStairs(self, n: int) -> int:
        if ( n <= 3):
            return n
        n1 = 1
        n2 = 1
        n -= 2
        while n >= 0 :
            tmp = n1
            n1 = n1 + n2
            n2 = tmp
            n -= 1
        return n1
