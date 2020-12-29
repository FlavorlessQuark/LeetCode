import re

class Solution:
    def myAtoi(self, s: str) -> int:
        number = re.findall(r'^[+-]?\d+', s.strip())
        if not number:
            return 0
        n = int(number[0])
        if n < -2147483648:
            return -2147483648
        elif n > 2147483647:
            return 2147483647
        return n
