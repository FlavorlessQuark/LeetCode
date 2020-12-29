class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, number in enumerate(nums):
            remainder = target - number
            if remainder in seen:
                return [seen[remainder], i]
            seen[number] = i
