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

    
    class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maximum = 0
        start = 0
        dp = {}
        for i in range(len(s)):
            if (s[i] in dp and dp[s[i]] >= start):
                start = dp[s[i]] + 1
                # print("IS there", s[i], start)
            # else:
            maximum = max(maximum, (i + 1) - start)
            dp[s[i]] = i
            # print(dp, maximum, s[i], start, i)
        return maximum
