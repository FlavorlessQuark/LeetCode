class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        high = len(nums)
        low = 0

        while high > low :
            current = (high + low) //2

            if (target == nums[current]) :
                return current

            if target > nums[current] :
                low = current + 1
            else :
                high = current

            # print(high, low, current)
        return low
