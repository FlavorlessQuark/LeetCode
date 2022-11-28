class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums)

        while (low < high):
            curr = low + ((high - low) // 2)
            if (nums[curr] == target):
                return curr
            if (nums[curr] > target):
                high = curr
            elif (nums[curr] < target):
                low = curr + 1
        else :
            return -1
        return low
