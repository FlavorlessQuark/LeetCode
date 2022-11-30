class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        s = sorted(nums)
        i = 0
        n = s[0]
        for x in s:
            if x == n:
                s[i] = x
                i += 1
            else:
                i = 0
                n = x
        return s[len(nums) // 2]
