# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        high = n
        low = 1
        while (low < high):
            current = low + ((high - low) // 2)
            if (isBadVersion(current)):
                high = current
            else :
                low = current + 1
        return low
