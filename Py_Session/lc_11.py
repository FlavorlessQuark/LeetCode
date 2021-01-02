class Solution:
    def maxArea(self, height: List[int]) -> int:
        m = 0
        start = 0
        end = len(height) - 1
        while start < end:
            m = max(m, (end - start) * min(height[start], height[end]))
            if height[start] < height[end]:
                start += 1
            else:
                end -= 1
        return m
