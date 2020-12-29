import itertools

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        for i, tup in enumerate(itertools.zip_longest(*strs)):
            if len(set(tup)) > 1:
                return strs[0][:i]
        return strs[0]
