import re

class Solution:
    def isNumber(self, s: str) -> bool:
        s = s.strip()
        if not s or s[0] == 'e':
            return False
        return bool(re.match(r'^(([+-])?\d+(?![+-]))?((?(2)((\d+\.)|([+-]?\.\d+))|([+-]?\d+\.|([+-]?\.\d+))))?(e[+-]?\d+)?$', s))
