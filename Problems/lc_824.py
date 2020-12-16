class Solution:
    def toGoatLatin(self, S: str) -> str:
        s = []
        for i, x in enumerate(S.split()):
            s.append(((x[1:] + x[0]) if x[0].lower() not in 'aeiou' else x) + 'ma' + 'a' * (i + 1))
        return ' '.join(s)
