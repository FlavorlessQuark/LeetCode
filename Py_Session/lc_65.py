import re

class Solution:
    def isNumber(self, s: str) -> bool:
        s = s.strip()
        if not s or s[0] == 'e':
            return False
        