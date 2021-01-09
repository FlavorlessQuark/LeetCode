import itertools
from functools import reduce
#  Note: This isn't fast compared to other submissions, but most of them actually convert the string to an int which was prohibited in the prompt

class Solution:

    def add(self, num1: str, num2: str) -> str:
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



    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == "0":
            return "0"
        r1, r2 = "".join(reversed(num1)), "".join(reversed(num2))

        tmp = []
        carry = 0
        m = 0
        print(r1, r2)
        for v1 in r2:
            total = ""
            carry = 0
            for v2 in r1:
                addition = (ord(v1) - ord('0')) * (ord(v2) - ord('0')) + carry
                carry = 0
                if addition >= 10:
                    carry = addition // 10
                    addition %= 10
                total = str(addition) + total

            if carry:
                total = str(carry) + total
            total += '0' * m
            m += 1
            tmp.append(total)
        print(tmp)
        s = reduce(self.add, tmp)
        return s
