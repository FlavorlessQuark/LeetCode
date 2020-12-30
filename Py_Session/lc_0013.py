class Solution:
    def romanToInt(self, s: str) -> int:
        table = {
                "I":1,
                "V":5,
                "X":10,
                "L":50,
                "C":100,
                "D":500,
                "M":1000
                }
        total = 0
        prev = 'I'
        for x in s[::-1]:
            if table[prev] > table[x]:
                total -= table[x]
            else:
                total += table[x]
            prev = x

        return total
