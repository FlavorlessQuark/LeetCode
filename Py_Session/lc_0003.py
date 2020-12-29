from collections import defaultdict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        letters = defaultdict(list)

        start = 0
        count = 0
        result = 0
        for end in range(start, len(s)):
            if s[end] in letters and s[end] in s[start:end]:
                result = max(result, count)
                start = letters[s[end]][-1] + 1
                count = end - start
            letters[s[end]] += [end]
            count += 1

        return max(result, count)
