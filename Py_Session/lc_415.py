import itertools

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        r1, r2 = reversed(num1), reversed(num2)

        total = ""
        carry = 0

        for v1, v2 in itertools.zip_longest(r1, r2, fillvalue='0'):
            addition = (ord(v1) - ord('0')) + (ord(v2) - ord('0')) + carry
            carry = 0
            if addition >= 10:
                addition -= 10
                carry = 1
            total += str(addition)
        if carry:
            total += str(carry)
        return "".join(reversed(total))
