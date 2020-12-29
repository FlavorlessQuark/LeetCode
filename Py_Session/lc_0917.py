class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        rev = "".join([x for x in S[::-1] if str.isalpha(x)])
        i = 0
        result = ""
        for char in S:
            if str.isalpha(char):
                result += rev[i]
                i += 1
            else:
                result += char
        return result
