class Solution:
    def distributeCandies(self, candy: List[int]) -> int:
        n = len(candy) // 2
        c = len(set(candy))
        if (n < c) : return n
        return c
