class Solution:
    def printVertically(self, s: str) -> List[str]:
        sep = s.split()
        words = []
        for x in itertools.zip_longest(*sep, fillvalue=" "):
            words.append(''.join(x).rstrip())
        return words
