class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        current = 0

        for n in nums:
            if (n != val):
                nums[current] = n
                current += 1
        return current
