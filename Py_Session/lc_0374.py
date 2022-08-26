# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        low = 1
        high = n
        while (1):
            current = low + (high - low) // 2
            res = guess(current)
            if (res == 0):
                return current
            if (res > 0):
                low = current + 1
            else :
                high = current
