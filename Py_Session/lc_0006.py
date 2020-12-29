class Solution:
    def convert(self, s: str, r: int) -> str:
        if r <= 1 or len(s) < r:
            return s
        result = [""] * r

        i = 0
        x = 1
        for char in s:
            result[i] += char
            i += x
            if i == 0 or i == (r - 1):
                x = -x
        return "".join(result)
