class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        current = 0

        for n in nums:
            if (nums[current] < n):
                current += 1
                nums[current] = n
        return current + 1
